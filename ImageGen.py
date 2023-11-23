import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

print("Welcome to ImageGen")
response = client.images.generate(prompt=" Hi def image of a couple dancing tango\n\n",
size="1024x1024")
image_url = response["data"]
print(image_url)"