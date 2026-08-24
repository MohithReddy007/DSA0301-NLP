from openai import OpenAI

client = OpenAI()

prompt = "Explain natural language processing in simple words."

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print(response.output_text)
