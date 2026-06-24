from google import genai
from dotenv import load_dotenv
from memory import add_memory, get_memory

import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    add_memory(user_input)

    memory = "\n".join(get_memory())

    prompt = f"""
Previous memory:
{memory}

Current user message:
{user_input}

Answer the user.
"""
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\nAI:", response.text)
