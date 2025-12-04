# test_embedding_model.py
from utils.embedding_model import generate_embeddings
from utils.text_splitter import split_text
from utils.document_loader import load_document
import os

def test_embedding():
    sample_file = "data/uploads/sample.txt"

    if not os.path.exists(sample_file):
        print(f"⚠️ File not found: {sample_file}. Please add a test file first.")
        return

    # Step 1: Load text
    print(f"\n🔍 Loading document: {sample_file}")
    text = load_document(sample_file)
    print(f"✅ Loaded {len(text)} characters.\n")

    # Step 2: Split into chunks
    chunks = split_text(text, chunk_size=300, overlap=50)
    print(f"✂️ Created {len(chunks)} chunks.\n")

    # Step 3: Generate embeddings
    embeddings = generate_embeddings(chunks)

    print(f"✅ Generated {len(embeddings)} embeddings.")
    print(f"Each embedding has {len(embeddings[0])} dimensions.\n")

    # Show preview
    print("🔹 First 5 values of the first embedding vector:")
    print(embeddings[0][:5])

if __name__ == "__main__":
    test_embedding()
