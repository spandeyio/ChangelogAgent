# Changelog Agent

A developer-facing conversational agent built with FastAPI, LangChain, and Gemini to answer questions about Anthropic's Claude product evolution based on a provided knowledge base.

## Prerequisites
- Python 3.12+
- `uv` package manager

## Setup and Run

1. Clone or extract the repository.
2. Install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```
   *Note: If you haven't synced requirements, you can run `uv sync` or use the installed packages directly from the `.venv`.*
3. Ensure `.env` is present with:
   ```
   GEMINI_API_KEY
   
   ```
4. Run the application:
   ```bash
   uv run uvicorn main:app --reload
   ```

## Usage

1. Open http://localhost:8000 in your browser.
2. Upload the `anthropic_changelog_kb.md` file using the upload section.
3. Chat with the agent about Claude's history!
