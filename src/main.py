from ollama import chat

stream = chat(
    model="deepseek-r1:1.5b",
    messages=[{"role": "user", "content": "Why is the sky blue?"}],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
