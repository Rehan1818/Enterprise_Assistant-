# test_vector_store.py
from utils.document_loader import load_document
from utils.text_splitter import split_text
from utils.embedding_model import generate_embeddings
from utils.vector_store import save_faiss_index, load_faiss_index
import numpy as np
import faiss
import os

def test_vector_store():
    sample_file = "data/uploads/sample.txt"

    if not os.path.exists(sample_file):
        print(f"⚠️ File not found: {sample_file}. Please add a test file first.")
        return

    print(f"\n🔍 Loading document: {sample_file}")
    text = load_document(sample_file)
    chunks = split_text(text, chunk_size=300, overlap=50)
    print(f"✂️ Split into {len(chunks)} chunks.")

    embeddings = generate_embeddings(chunks)
    print(f"✅ Generated {len(embeddings)} embeddings.")

    # Save FAISS index
    print("\n💾 Saving FAISS index...")
    save_faiss_index(chunks, embeddings, index_name="sample_index")

    # Load FAISS index
    print("\n📂 Loading FAISS index...")
    index, saved_chunks = load_faiss_index("sample_index")

    # Verify
    print(f"✅ Loaded {len(saved_chunks)} chunks from saved metadata.")

    # Perform a test search
    print("\n🔍 Performing test similarity search...")
    query_vector = np.array([embeddings[0]]).astype("float32")
    D, I = index.search(query_vector, k=2)  # top 2 similar chunks

    print(f"🔹 Top 2 matching indices: {I[0]}")
    print(f"🔹 Distance scores: {D[0]}")

    # Show matched chunks
    for idx in I[0]:
        print(f"\n📄 Match: {saved_chunks[idx][:200]}...")

if __name__ == "__main__":
    test_vector_store()
