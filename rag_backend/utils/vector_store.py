import faiss
import numpy as np
import os
import pickle

VECTOR_DIR = "data/vector_store"
os.makedirs(VECTOR_DIR, exist_ok=True)

def save_faiss_index(chunks, embeddings, index_name="default_index"):
   
    index_path = os.path.join(VECTOR_DIR, f"{index_name}.index")
    metadata_path = os.path.join(VECTOR_DIR, f"{index_name}_meta.pkl")

    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, index_path)

    with open(metadata_path, "wb") as f:
        pickle.dump(chunks, f)

    print(f" Saved FAISS index to {index_path}")
    print(f"Saved metadata to {metadata_path}")

    return {"index_path": index_path, "metadata_path": metadata_path}


def load_faiss_index(index_name="default_index"):
    """
    Loads a FAISS index and its metadata (chunks) from disk.
    """
    index_path = os.path.join(VECTOR_DIR, f"{index_name}.index")
    metadata_path = os.path.join(VECTOR_DIR, f"{index_name}_meta.pkl")

    if not os.path.exists(index_path) or not os.path.exists(metadata_path):
        raise FileNotFoundError(f"Index or metadata file not found for '{index_name}'")

    index = faiss.read_index(index_path)

    with open(metadata_path, "rb") as f:
        chunks = pickle.load(f)

    print(f" Loaded FAISS index ({len(chunks)} chunks)")
    return index, chunks
