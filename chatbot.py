import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client=OpenAI(
    api_key=os.getenv("Bot_API"),
    base_url="https://api.groq.com/openai/v1"
)
response=client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role":"user",
            "content":"suggest two titles for instructional lessons on chat applications in AI"
        }
    ]
)
print(response.choices[0].message.content)