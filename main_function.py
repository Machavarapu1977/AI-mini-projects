from search_index import Search_videos
from Groq_model import ask_groq
query="AI tutorial"
results=Search_videos(query)
print("Relevant Videos:\n")
for videos in results:
    print(videos)
context="\n".join(results)
prompt=f"""
User searched for: {query}
relevant videos:
{context}
Explain why these videos are a match
"""
answer=ask_groq(prompt)
print("\nGroq's Response\n")
print(answer)