import openai
from apikey import APIKEY

openai.api_key = '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'

output = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)
print(output)