import os
from dotenv import load_dotenv
from openai import OpenAI 

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "user",
            "content": """
you are a helpful ai assistand who returns output only in JSON format.
"""
        },
        {
            "role": "user",
            "content": "give me list of most popular one piece characters and their pirate crew and gender in json format."
        }
    ]
)

print(response.choices[0].message.content)
