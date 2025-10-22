from nlp.sql_generator import generate_sql
from db.query_executor import run_query
from nlp.response_formatter import format_response
from utils.logger import log
from utils.helpers import sanitize_user_input
# Chatbot main function
def chatbot():
    print("🚴 Welcome to Bike Store SQL Chatbot!")
    print("Ask anything about orders, staffs, or customers.\n(Type 'exit' to quit.)\n")
# Main interaction loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye 👋")
            break

# Sanitize user input to prevent SQL injection(cleaning user input)
        user_input = sanitize_user_input(user_input)
        log(f"User Query: {user_input}")
# Generate SQL from user input(prompt+user input+model will go to llm to generate sql query)
        sql_query = generate_sql(user_input)
        log(f"Generated SQL: {sql_query}")
# Execute the SQL query(run query send sql to db and get results)
        results = run_query(sql_query)
# Format the database response(formatting results to readable format)
        response = format_response(results)
        print(f"\nBot:\n{response}\n")
# Log the response
if __name__ == "__main__":
    chatbot()
