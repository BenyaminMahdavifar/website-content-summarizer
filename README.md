# Website Content Summarizer

> Extract, summarize, and chat with website content using local or cloud LLMs.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![LLM](https://img.shields.io/badge/LLM-OpenRouter%20%7C%20Ollama-orange)

---

## Overview

Website Content Summarizer is a Python application that extracts textual content from web pages and uses Large Language Models (LLMs) to generate summaries and answer questions about website content.

The project supports both cloud-based models through OpenRouter and local models through Ollama, allowing users to choose between remote and fully local inference.

---

## Motivation

Large web pages often contain unnecessary HTML, navigation menus, advertisements, and boilerplate content that make them difficult to analyze with language models.

This project provides a simple pipeline:

1. Download webpage content.
2. Remove irrelevant HTML elements.
3. Extract the meaningful text.
4. Send the content to an LLM.
5. Generate summaries or answer questions.

---

## Features

* Website content extraction
* HTML cleaning and text processing
* Automatic summarization
* Question answering over webpage content
* Interactive chat workflow
* OpenRouter integration
* Ollama integration
* Local and cloud LLM support
* Simple configuration using environment variables

---

## Supported Backends

| Backend    | Description                             |
| ---------- | --------------------------------------- |
| OpenRouter | Access cloud LLMs through a unified API |
| Ollama     | Run local models on your machine        |
| OpenAI SDK | Compatible client interface             |

Supported models include:

* DeepSeek R1
* Llama 3.2
* OpenRouter models
* Ollama local models

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

## Configuration

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

Example output:

```text
Summary:
OpenAI is an artificial intelligence research and deployment company.

Answer:
The website describes OpenAI's products, research, and AI technologies.
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

## Technologies

* Python
* BeautifulSoup
* Requests
* OpenAI SDK
* OpenRouter
* Ollama

---

## Future Improvements

* Multi-page crawling
* Retrieval-Augmented Generation (RAG)
* Conversation memory
* Vector database support
* PDF export
* Streamlit web interface

---

## License

MIT

---

## Author

**Benyamin Mahdavifar**

GitHub: https://github.com/BenyaminMahdavifar
