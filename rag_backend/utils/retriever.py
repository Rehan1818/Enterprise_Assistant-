import faiss
import pickle
import numpy as np
from utils.embedding_model import generate_embeddings

def load_index(index_path):
    return faiss.read_index(index_path)

def load_metadata(metadata_path):
    with open(metadata_path, "rb") as f:
        return pickle.load(f)

def retrieve(query, index_path, metadata_path, top_k=3):
    # Load index + metadata
    index = load_index(index_path)
    metadata = load_metadata(metadata_path)

    # Generate embedding for user query
    query_embedding = generate_embeddings([query])[0].reshape(1, -1)

    # Perform similarity search
    distances, indices = index.search(query_embedding, top_k)

    # Collect results
    results = []
    for idx, score in zip(indices[0], distances[0]):
        if idx == -1:
            continue
        results.append({
            "chunk": metadata[idx],
            "score": float(score)
        })

    return results
