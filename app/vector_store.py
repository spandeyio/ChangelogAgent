from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import faiss
import uuid
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from pypdf import PdfReader
from app.config import settings

class VectorStoreManager:
    def __init__(self):
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-2-preview", 
            google_api_key=settings.GEMINI_API_KEY
        )
        self.index = faiss.IndexFlatL2(len(self.embeddings.embed_query("test")))
        self.vector_store = FAISS(
            embedding_function=self.embeddings,
            index=self.index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )
    
    def add_file_to_store(self, file_path: str) -> int:
        ext = os.path.splitext(file_path)[1].lower()
        text = ""
        if ext == ".md":
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        elif ext == ".pdf":
            reader = PdfReader(file_path)
            text = "".join(page.extract_text() for page in reader.pages)
        
        if text:
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = text_splitter.split_text(text)
            docs = [Document(page_content=chunk, metadata={"source": file_path}) for chunk in chunks]
            uuids = [str(uuid.uuid4()) for _ in range(len(docs))]
            # Add documents one by one to avoid embedding batch length issues
            for doc, doc_uuid in zip(docs, uuids):
                self.vector_store.add_documents(documents=[doc], ids=[doc_uuid])
            return len(docs)
        return 0

    def query_vector_store(self, query: str) -> str:
        docs = self.vector_store.similarity_search(query, k=5)
        if not docs:
            return "No relevant information found in the knowledge base."
        return "\n\n".join(f"Source: {doc.metadata.get('source', '')}\nContent: {doc.page_content}" for doc in docs)

vector_store_manager = VectorStoreManager()
