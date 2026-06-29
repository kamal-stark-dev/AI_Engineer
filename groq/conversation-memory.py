import os
from dotenv import load_dotenv 
from openai import OpenAI 

load_dotenv()

messages=[
    {
        "role": "system",
        "content": "You are an anime expert assistant. Also you don't reply to question that are not anime related and politely tell them that you can't help with non-anime topics."
    }
]

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    answer = response.choices[0].message.content 

    print("\nAssistant:", answer)

    messages.append({
        "role": "assistant",
        "content": answer
    })

print("Messages:", messages)
