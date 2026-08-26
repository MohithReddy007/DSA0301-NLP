from google import genai

# Enter your Gemini API key
client = genai.Client(api_key="AQ.Ab8RN6IOKrgs4zbfIGmb4qa5fRTNmbAzPB2W89DWTZvbNzIi6Q")

prompt = "Write a short paragraph about Artificial Intelligence."

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("Prompt:")
    print(prompt)

    print("\nGenerated Text:")
    print(response.text)

except Exception as e:
    print("Error:", e)
