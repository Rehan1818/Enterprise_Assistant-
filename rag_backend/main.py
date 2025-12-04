# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
from utils.document_loader import load_document
from utils.text_splitter import split_text
from utils.embedding_model import generate_embeddings
from utils.vector_store import save_faiss_index
from utils.retriever import retrieve
from utils.retriever import retrieve
from utils.generator import generate_answer


# Create upload and vector directories
UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI(title="RAG Indexing API", version="1.0")

# Enable CORS (so React frontend can connect later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to the RAG Indexing API 🚀"}

@app.post("/index")
async def index_document(file: UploadFile = File(...)):
    """
    Upload a document (PDF, DOCX, TXT), index it, and store in FAISS.
    """
    # Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # --- Run the indexing pipeline ---
    text = load_document(file_path)
    chunks = split_text(text, chunk_size=500, overlap=100)
    embeddings = generate_embeddings(chunks)
    index_name = os.path.splitext(file.filename)[0]
    result = save_faiss_index(chunks, embeddings, index_name=index_name)

    return {
        "message": "Indexing completed successfully",
        "index_path": result["index_path"],
        "metadata_path": result["metadata_path"],
        "total_chunks": len(chunks)
    }

@app.get("/retrieve")
def retrieve_answer(query: str, index_name: str = "sample", top_k: int = 3):
    index_path = f"data/vector_store/{index_name}.index"
    metadata_path = f"data/vector_store/{index_name}_meta.pkl"

    results = retrieve(query, index_path, metadata_path, top_k)
    return {"query": query, "results": results}

@app.get("/rag")
def rag_pipeline(query: str, index_name: str = "sample", top_k: int = 3):
    # Paths
    index_path = f"data/vector_store/{index_name}.index"
    metadata_path = f"data/vector_store/{index_name}_meta.pkl"

    # Step 1: Retrieve relevant chunks
    retrieved_chunks = retrieve(query, index_path, metadata_path, top_k)

    # Step 2: Generate final answer using Gemini
    final_answer = generate_answer(query, retrieved_chunks)

    return {
        "query": query,
        "answer": final_answer,
        "chunks_used": retrieved_chunks
    }
