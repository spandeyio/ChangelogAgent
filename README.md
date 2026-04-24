<div align="center">
  <h1>🚀 Changelog Agent</h1>
  <p><i>A developer-facing conversational agent built with FastAPI, LangChain, and Gemini to answer questions about Anthropic's Claude product evolution based on a provided knowledge base.</i></p>

  [![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
  [![LangChain](https://img.shields.io/badge/LangChain-1.2.15-1a1a1a.svg)](https://www.langchain.com/)
  [![FAISS](https://img.shields.io/badge/FAISS-CPU-yellow.svg)](https://github.com/facebookresearch/faiss)
</div>

<br />

---

## 📖 Overview

The **Changelog Agent** is a sophisticated RAG (Retrieval-Augmented Generation) web application that empowers developers to interactively query Anthropic's Claude product history. Upload markdown or PDF documentation, and the agent accurately pulls contextual information from the FAISS vector store to formulate pristine, HTML-formatted responses.

### ✨ Key Features
- **Upload Knowledge Bases:** Process `.md` or `.pdf` files efficiently into vector chunks.
- **Conversational Memory:** Retains the last 10 messages of the chat history to provide continuous conversational context.
- **Agentic Tools:** The LLM independently invokes search tools only when required.
- **Modern Developer UI:** A subtle, beautiful, and highly polished chat dashboard styled with developer rhythm.

---

## 🛠️ Architecture

* **Backend:** `FastAPI` (serving REST endpoints and static files)
* **Orchestration:** `LangChain` Agents
* **Vector Store:** `FAISS` (Facebook AI Similarity Search)
* **Embeddings:** `Google Generative AI` (`gemini-embedding-2-preview`)
* **LLM Engine:** `Gemini 1.5 Flash` via Google Generative AI
* **Frontend:** Vanilla HTML, CSS (Custom Inter Theme), and JavaScript

---

## ⚙️ Prerequisites

To run this application locally, you will need:
- **Python 3.12+**
- **`uv`** package manager (for ultra-fast dependency resolution)

---

## 🚀 Setup and Run

**1. Clone the repository**
```bash
git clone https://github.com/spandeyio/ChangelogAgent.git
cd ChangelogAgent
```

**2. Setup Virtual Environment and Install Dependencies**
```bash
# Initialize uv virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies from the existing project configuration
uv sync
```

**3. Configure Environment Variables**
Create a `.env` file in the root directory and add your API keys:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

**4. Start the Application**
```bash
uv run uvicorn main:app --reload --port 8000
```
*The server will start at `http://127.0.0.1:8000`.*

---

## 💻 Usage Guide

1. **Launch the Dashboard**: Open your web browser and navigate to http://localhost:8000.
2. **Upload Documentation**: Use the left sidebar to upload your `anthropic_changelog_kb.md` file. Wait for the success confirmation.
3. **Ask Questions**: Ask the agent anything! For example:
   * *"When was Claude 3.5 Sonnet released?"*
   * *"What are the breaking changes in the latest API version?"*
   * *"Show me the pricing for Claude Haiku."*

---

<div align="center">
  <p>Built with ❤️ for AI Engineering.</p>
</div>
