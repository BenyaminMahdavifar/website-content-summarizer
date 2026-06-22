from scraper import fetch_website_contents
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

website = input("Website URL: ")
content = fetch_website_contents(website)

messages = [
    {
        "role": "system",
        "content":
        f"You answer questions about this website:\n{content}"
    }
]

while True:
    question = input("\nQuestion (exit to quit): ")

    if question.lower() == "exit":
        break

    messages.append(
        {"role": "user", "content": question}
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=500
    )

    answer = response.choices[0].message.content

    print("\nAssistant:\n")
    print(answer)

    messages.append(
        {"role": "assistant", "content": answer}
    )