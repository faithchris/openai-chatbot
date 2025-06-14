import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_prompt = input("whatt do you want to ask? ")

system_prompt = "You are a helpful assistant."

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print("Response:", response.choices[0].message.content.strip())
# This code initializes an OpenAI client, takes a user prompt, and generates a response using the GPT-4o model.