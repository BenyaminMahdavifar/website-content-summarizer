# Website Content Summarizer

> Chat with website content using OpenRouter and Ollama.

A Python application that extracts website content and uses Large Language Models (LLMs) to summarize and answer questions about web pages.

---

## Features

- Website content extraction
- Automatic HTML cleaning
- Website summarization
- Question answering
- Interactive chat
- OpenRouter support
- Ollama support
- Local and cloud LLMs

---

## Installation

Clone the repository:

```bash
git clone https://github.com/BenyaminMahdavifar/website-content-summarizer.git

cd website-content-summarizer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

### OpenRouter

```env
BASE_URL=https://openrouter.ai/api/v1
API_KEY=your_api_key
MODEL=deepseek/deepseek-r1
```

### Ollama

```env
BASE_URL=http://localhost:11434/v1
API_KEY=ollama
MODEL=llama3.2:3b
```

---

## Usage

Run the application:

```bash
python app.py
```

Example:

```text
Website URL:
https://openai.com

Question:
What is this website about?
```

---

## Project Structure

```text
website-content-summarizer/
│
├── app.py
├── scraper.py
├── requirements.txt
├── .env.example
├── README.md
└── examples/
    ├── openrouter.py
    └── ollama.py
```

---

## Supported Models

- DeepSeek R1
- Llama 3.2
- OpenRouter models
- Ollama local models

---

## Technologies

- Python
- BeautifulSoup
- Requests
- OpenAI SDK
- OpenRouter
- Ollama

---

## License

MIT
