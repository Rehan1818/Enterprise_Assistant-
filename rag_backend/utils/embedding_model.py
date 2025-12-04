from sentence_transformers import SentenceTransformer

def get_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks):
    model = get_embedding_model()
    embeddings = model.encode(chunks, convert_to_tensor=False)
    return embeddings
