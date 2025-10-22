from nlp.sql_generator import generate_sql
from db.query_executor import run_query
from nlp.response_formatter import format_response
from utils.logger import log
from utils.helpers import sanitize_user_input

def chatbot():
    print("🚴 Welcome to Bike Store SQL Chatbot!")
    print("Ask anything about orders, staffs, or customers.\n(Type 'exit' to quit.)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye 👋")
            break

        user_input = sanitize_user_input(user_input)
        log(f"User Query: {user_input}")

        sql_query = generate_sql(user_input)
        log(f"Generated SQL: {sql_query}")

        results = run_query(sql_query)
        response = format_response(results)
        print(f"\nBot:\n{response}\n")

if __name__ == "__main__":
    chatbot()
