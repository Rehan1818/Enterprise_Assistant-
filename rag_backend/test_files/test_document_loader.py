from utils.document_loader import load_document
import os

def test_loader():
    test_files = [
        "data/uploads/sample.pdf"
    ]

    for file_path in test_files:
        if os.path.exists(file_path):
            print(f"\n🔍 Testing file: {os.path.basename(file_path)}")
            try:
                text = load_document(file_path)
                print(f"✅ Successfully loaded {len(text)} characters of text.")
                print(f"Preview: {text[:300]}...\n")
            except Exception as e:
                print(f"❌ Error reading {file_path}: {e}")
        else:
            print(f"⚠️ File not found: {file_path}. Please place a test file here.")

if __name__ == "__main__":
    test_loader()
