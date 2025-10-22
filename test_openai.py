import openai

openai.api_key = "REMOVEDproj-3U-RaRqTODFioNMPfKiAjQsMJptD_HtTqlJ9S4Y6u8V21p-XyZuqKvo7lhKUuQvViiCkB_ATbwT3BlbkFJyF9ceilXBVkpLKD-gaJzTTd4RXy1En5AeXx9jbzM5OnGs-8MSghRhi-5s45JO4O0uoFXfTOwEA"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use GPT-3.5 instead of GPT-4
    messages=[{"role": "user", "content": "Say hello"}]
)
print(response.choices[0].message.content)
