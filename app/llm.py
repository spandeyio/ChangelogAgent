from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import settings


class LLM:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.1-flash-lite-preview",
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0,
        )

    def get_llm(self):
        return self.llm


llm_instance = LLM()
