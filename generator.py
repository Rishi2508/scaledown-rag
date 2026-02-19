# generator.py

from google import genai
import os

# Read API key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not set!")

client = genai.Client(api_key=api_key)


def generate_answer(query, retrieved_chunks):

    if not retrieved_chunks:
        return "No relevant code found for this question."

    context = "\n\n".join(
        [f"File: {chunk['path']}\n{chunk['content']}" for chunk in retrieved_chunks]
    )

    prompt = f"""
You are a senior Python codebase analyst.

Answer using ONLY the provided context.

Be detailed and technical.

Context:
{context}

Question:
{query}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error generating response: {str(e)}"
