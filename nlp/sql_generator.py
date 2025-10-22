import google.generativeai as genai
from config import GOOGLE_API_KEY
from nlp.prompt_templates import BIKESTORE_PROMPT

genai.configure(api_key=GOOGLE_API_KEY)

# Use a valid Gemini text-generation model
MODEL_NAME = "models/gemini-flash-latest"
# Function to generate SQL query from user input
def generate_sql(user_input: str):
    prompt = BIKESTORE_PROMPT.format(user_query=user_input)
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        sql_query = response.text.strip()
        return sql_query
    except Exception as e:
        return f"-- Error generating SQL: {e}"
