import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Tool definition
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather of a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

# Python function
def get_weather(city):
    return f"The weather in {city} is sunny, 28°C."

messages = [
    {
        "role": "user",
        "content": "What's the weather in Paris?"
    }
]

# First request
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

message = response.choices[0].message

# Add assistant response
messages.append(message)

# Check if the model wants to call a tool
if message.tool_calls:
    tool_call = message.tool_calls[0]

    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    if function_name == "get_weather":
        result = get_weather(arguments["city"])

        # Send tool result back
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            }
        )

        # Second request
        final_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
        )

        print(final_response.choices[0].message.content)

else:
    print(message.content)
