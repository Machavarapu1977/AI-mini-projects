import requests
from PIL import Image
from urllib.parse import quote
from io import BytesIO
prompt="A realistic orange cat sitting beside a rainy cyberpunk window, cinematic lighting"
encoded_prompt=quote(prompt)
url=f"https://image.pollinations.ai/prompt/{encoded_prompt}/"
response=requests.get(url)
print(response.headers["content-type"])
image=Image.open(BytesIO(response.content))
image.save("image.jpg")
image.show()