# chatbot_project/llm/config.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_llm():
    """Initializes and returns the Google Generative AI LLM."""
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY environment variable not set.")
    
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.0) # temperature=0.0 for more deterministic responses
    return llm

if __name__ == "__main__":
    try:
        llm = get_llm()
        print("LLM initialized successfully.")
        # Example of using the LLM (optional, just for testing)
        # from langchain_core.messages import HumanMessage
        # response = llm.invoke([HumanMessage(content="Hello, how are you?")])
        # print(response.content)
    except ValueError as e:
        print(f"Error: {e}")