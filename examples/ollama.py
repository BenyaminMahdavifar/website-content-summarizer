# ollama_example

from openai import OpenAI
from scraper import fetch_website_contents

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

content = fetch_website_contents(
    "https://openai.com"
)

response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": f"Answer questions about:\n{content}"
        },
        {
            "role": "user",
            "content": "What is this website about?"
        }
    ]
)

print(response.choices[0].message.content)