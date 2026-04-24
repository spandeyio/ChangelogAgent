from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import shutil
from typing import List, Dict
from langchain_core.messages import HumanMessage, AIMessage

from app.agent import changelog_agent
from app.vector_store import vector_store_manager

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class ChatRequest(BaseModel):
    query: str
    history: List[Dict[str, str]]

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith((".md", ".pdf")):
        raise HTTPException(status_code=400, detail="Only .md and .pdf files are allowed.")
    
    try:
        os.makedirs("uploads", exist_ok=True)
        file_path = f"uploads/{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        docs_added = vector_store_manager.add_file_to_store(file_path)
        return {"message": f"Successfully processed {file.filename} and added {docs_added} chunks to vector store."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process file: {str(e)}")

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        history_to_use = request.history[-20:]
        response = changelog_agent.invoke(request.query, history_to_use)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {str(e)}")
