import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
client=genai.Client(
    api_key=os.environ["Gemini_api_key"]
)
prompt="You are an expert python instructor. Tell me about lists in the following format: definition, syntax, example usage, importance, simple example and it's dry run"
messages=[
    {
        "role":"user",
        "content": prompt
    }
]
response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages[0]["content"]
)
print(response.text)
