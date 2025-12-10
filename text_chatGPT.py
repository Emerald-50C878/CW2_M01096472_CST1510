from openai import OpenAI
import bcrypt

client = OpenAI(api_key="your-api-key-here")

prompt = "Hello, how are you today?"

completion = client.chat.completions.create(
    model="gpt-5.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)
print(completion.choices[0].message.content)