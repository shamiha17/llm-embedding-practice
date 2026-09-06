from groq import Groq

client = Groq(
    api_key="gsk_xxxxxxxx"
)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Explain machine learning in simple English."
        }
    ]
)

print(response.choices[0].message.content)