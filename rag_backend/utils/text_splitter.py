from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(text: str, chunk_size=1000, overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\n\n", "\n", ".", "!", "?", " "],
    )
    return splitter.split_text(text)
