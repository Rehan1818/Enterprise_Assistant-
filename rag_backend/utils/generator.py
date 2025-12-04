import google.generativeai as genai
import os

# Load Gemini Key from ENV or hardcode temporarily
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_answer(query, retrieved_chunks):
    """
    Takes raw chunks and query → sends to Gemini → returns final answer.
    """

    context_text = "\n\n".join([
        f"Chunk {i+1}:\n{chunk['chunk']}"
        for i, chunk in enumerate(retrieved_chunks)
    ])

    prompt = f"""
You are an expert assistant. Use ONLY the following document chunks to answer the question.
Do NOT hallucinate. If the answer cannot be found, say "The document does not contain this information."

Document Chunks:
{context_text}

Question:
{query}

Final Answer:
"""

    # Use Gemini 1.5 Flash (fast + cheap)
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)

    return response.text
