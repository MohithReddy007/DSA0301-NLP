"""
Experiment 25: GPT-Based Text Generation
Course: Natural Language Processing

Description:
This program demonstrates gpt-based text generation.

Author: Student
"""

# Set the OPENAI_API_KEY environment variable before running.
# Example on Windows PowerShell:
#   $env:OPENAI_API_KEY="your_api_key"

from openai import OpenAI

client = OpenAI()

prompt = "Explain natural language processing in simple words."

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print(response.output_text)
