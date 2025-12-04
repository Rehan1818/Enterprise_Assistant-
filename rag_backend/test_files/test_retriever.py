from utils.retriever import retrieve

index_path = "data/vector_store/sample.index"
metadata_path = "data/vector_store/sample_meta.pkl"

query = "What is the work from home policy?"

results = retrieve(query, index_path, metadata_path, top_k=3)

print("\n=== Retrieved Results ===")
for r in results:
    print("\nChunk:", r["chunk"])
    print("Score:", r["score"])
