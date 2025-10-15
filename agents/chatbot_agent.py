# chatbot_project/agents/chatbot_agent.py
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent
from llm.config import get_llm
from llm.tools import ALL_TOOLS # Import all tools

def get_chatbot_agent():
    """
    Initializes and returns a LangChain agent capable of interacting with the database tools.
    """
    llm = get_llm()

    # 1. Define the tools the agent can use
    tools = ALL_TOOLS

    # 2. Define the prompt
    # It's crucial to provide good instructions and context.
    # The 'tools' and 'tool_names' are automatically filled by LangChain.
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are a helpful assistant for a bike store database. "
         "You have access to tools to query information about customers, staff, and orders. "
         "First, get a summary of the database schema if you need to understand the tables. "
         "If a specific tool is not available for a query, try to use `execute_database_query` "
         "with a carefully crafted SQL SELECT statement. "
         "Always try to provide a clear and concise answer. If you can't find an answer, say so."),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ])

    # 3. Create the agent
    # This agent uses the LLM to decide which tool to call.
    agent = create_tool_calling_agent(llm, tools, prompt)

    # 4. Create the AgentExecutor
    # This runs the agent and executes the tools.
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True, # Set to True to see the agent's thought process
        handle_parsing_errors=True # Good for debugging
    )
    
    return agent_executor

# --- LangGraph (Optional, for more complex state management) ---
# For more advanced routing, loops, and conditional logic, LangGraph is ideal.
# Here's a conceptual outline. You'd typically define 'nodes' for each action
# (e.g., call tool, respond to user, check state) and 'edges' to connect them.

from typing import List, Tuple, Annotated, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver


class AgentState(TypedDict):
    """
    Represents the state of our graph.
    - messages: A list of messages in the conversation.
    - next: The next action to take.
    """
    messages: Annotated[List[BaseMessage], lambda x, y: x + y]
    # future: you might add things like `current_tool_output`, `context_data`

def create_langgraph_agent():
    llm = get_llm()
    tools = ALL_TOOLS
    tool_executor = AgentExecutor(
        agent=create_tool_calling_agent(llm, tools, prompt), # Reuse the prompt and agent logic
        tools=tools,
        verbose=False, # LangGraph will handle verbose logging
        handle_parsing_errors=True
    )

    # Define the nodes and edges for LangGraph
    graph_builder = StateGraph(AgentState)

    def call_tool(state: AgentState):
        # The agent calls a tool based on the current messages
        response = tool_executor.invoke({"input": state["messages"][-1].content, "chat_history": state["messages"][:-1]})
        return {"messages": [AIMessage(content=response["output"])]} # Wrap tool output as AIMessage
        
    def respond_to_user(state: AgentState):
        # Here, the LLM generates a final answer if no tool is needed or after tool output
        # For simplicity, we're assuming call_tool handles the final response or tool output.
        # In a real LangGraph, you might have a dedicated node for final response generation
        # based on tool results.
        return state # The previous node already added the AIMessage

    graph_builder.add_node("call_tool", call_tool)
    graph_builder.add_node("respond_to_user", respond_to_user)

    graph_builder.add_edge(START, "call_tool")
    graph_builder.add_edge("call_tool", END) # Simple direct flow for now
    # More complex routing would involve conditional edges (e.g., based on tool output)

    # If you want state persistence for conversation history
    memory = SqliteSaver.from_file("langgraph_memory.sqlite")
    
    graph = graph_builder.compile(checkpointer=memory)
    return graph

# Choose which agent to use in main.py
# For this example, we'll start with the simpler `get_chatbot_agent` (AgentExecutor).
# You can uncomment `create_langgraph_agent` and use it later.