# chatbot_project/main.py
import os
from dotenv import load_dotenv
from agents.chatbot_agent import get_chatbot_agent # Or create_langgraph_agent
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables
load_dotenv()

def main():
    try:
        # Initialize the chatbot agent
        agent_executor = get_chatbot_agent() # Using AgentExecutor for simplicity
        # If you want to use LangGraph:
        # agent_executor = create_langgraph_agent() # This would be compiled graph

        print("Chatbot initialized! Type 'exit' to quit.")
        print("You can ask questions like: 'How many orders are there?', 'Who is customer 1?', 'Show orders for customer 2'.")

        chat_history = []

        while True:
            user_input = input("\nYou: ")
            if user_input.lower() == 'exit':
                break

            try:
                # Invoke the agent
                # For AgentExecutor:
                response = agent_executor.invoke({
                    "input": user_input,
                    "chat_history": chat_history # Pass the full chat history
                })
                
                # For LangGraph (if using SqliteSaver for memory, the state is managed internally)
                # response = agent_executor.invoke({"messages": [HumanMessage(content=user_input)]})
                # agent_executor.invoke({"messages": [HumanMessage(content=user_input)]}, {"configurable": {"thread_id": "user-session-1"}})
                # You'd then fetch the latest message from the state for display
                # state = agent_executor.get_state({"configurable": {"thread_id": "user-session-1"}})
                # print("Chatbot:", state.messages[-1].content)


                ai_response_content = response["output"] # AgentExecutor output
                print(f"Chatbot: {ai_response_content}")

                # Update chat history for AgentExecutor
                chat_history.append(HumanMessage(content=user_input))
                chat_history.append(AIMessage(content=ai_response_content))

            except Exception as e:
                print(f"An error occurred: {e}")
                print("Please try rephrasing your question or check the database connection.")

    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("Please ensure your .env file is correctly set up with GOOGLE_API_KEY and MySQL credentials.")
    except Exception as e:
        print(f"An unexpected error occurred during chatbot initialization: {e}")

if __name__ == "__main__":
    main()