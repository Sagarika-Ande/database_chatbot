import google.generativeai as genai

genai.configure(api_key="AIzaSyCYmU3IZyf8d_aJ7Q3OJbq66hO8Bz_gvyY")

# Convert generator to list
all_models = list(genai.list_models())

# Pick a text-generation model manually
text_gen_model_name = "models/gemini-flash-latest"

model = genai.GenerativeModel(text_gen_model_name)

response = model.generate_content("Say hello world")
print("Generated text:", response.text)
