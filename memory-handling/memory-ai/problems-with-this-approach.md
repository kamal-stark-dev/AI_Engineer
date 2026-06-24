### The problem with this approach:

Imagine `memory.json` becomes:
```json
[
    "message1",
    "message2",
    "message3",
    ...
    "message5000"
]
```

Now every prompt sends these 5000 messages to your LLM (gemini in our case.)

**Problems**:
1. Slow
2. Expensive
3. Context window limits
4. Poor retrieval (relevant information can get mixed up with a lot of irrelevant information)

