import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client=Groq(api_key=os.getenv("Bot_API"))
student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."
student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
prompt1=f"""
please extract the following information from the written text and return it as a JSON object:
name
major
school
grades
club
This is the body of text to extract information from:
{student_1_description}
"""
prompt2=f"""
please extract the following information from the written text and return it as a JSON object:
name
major
school
grades
club
This is the body of text to extract information from:
{student_2_description}
"""
response1=client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role":"user",
            "content":prompt1
        }
    ]
)
print(response1.choices[0].message.content)
response2=client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role":"user",
            "content":prompt2
        }
    ]
)
print(response2.choices[0].message.content)