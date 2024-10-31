import openai

openai.base_url = "http://localhost:8080"
openai.api_key = "sk-no-key-required"

is_streaming = True

response = openai.chat.completions.create(
    model="default",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write an article about the weather of Seattle."}
    ],
    stream = is_streaming
)

if is_streaming:
    for chunk in response:
        print(chunk.choices[0].delta.content or "", end = "")
else:
    print(response.choices[0].message.content)
