from bs4 import BeautifulSoup
import requests

HEADERS = {
    "User-Agent":
    "Mozilla/5.0"
}


def fetch_website_contents(url, limit=2000):

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=10
    )

    soup = BeautifulSoup(
        response.content,
        "html.parser"
    )

    title = (
        soup.title.string
        if soup.title
        else "No title"
    )

    if soup.body:
        for tag in soup.body(
            ["script", "style", "img", "input"]
        ):
            tag.decompose()

        text = soup.body.get_text(
            separator="\n",
            strip=True
        )
    else:
        text = ""

    return (title + "\n\n" + text)[:limit]