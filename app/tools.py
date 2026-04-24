from langchain.tools import tool
from app.vector_store import vector_store_manager

@tool
def search_knowledge_base(query: str) -> str:
    """Search the vector store knowledge base for information about Anthropic Claude products."""
    return vector_store_manager.query_vector_store(query)

def get_tools():
    return [search_knowledge_base]
