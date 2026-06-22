# openrouter_example

from openai import OpenAI
from scraper import fetch_website_contents
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

content = fetch_website_contents(
    "https://openai.com"
)

response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role": "system",
            "content": f"Answer questions about:\n{content}"
        },
        {
            "role": "user",
            "content": "Summarize this website."
        }
    ]
)

print(response.choices[0].message.content)