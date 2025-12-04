# test_text_splitter.py
from utils.text_splitter import split_text
from utils.document_loader import load_document
import os

def test_splitter():
    sample_file = "data/uploads/sample.txt"

    if not os.path.exists(sample_file):
        print(f"⚠️ File not found: {sample_file}. Please add a sample file first.")
        return

    # Load document text
    print(f"\n🔍 Loading text from: {sample_file}")
    text = load_document(sample_file)
    print(f"✅ Loaded {len(text)} characters.")

    # Split into chunks
    print("\n✂️ Splitting text into chunks...")
    chunks = split_text(text, chunk_size=300, overlap=50)
    print(f"✅ Created {len(chunks)} chunks.\n")

    # Show sample output
    for i, chunk in enumerate(chunks[:3]):  # show first 3 chunks
        print(f"📦 Chunk {i+1}: ({len(chunk)} chars)")
        print(chunk[:200] + "...\n")

if __name__ == "__main__":
    test_splitter()
