# generator.py
from google import genai
import os

# Read API key from environment
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not set in environment!")

# Create a GenAI client
client = genai.Client(api_key=api_key)

def generate_answer(query, retrieved_chunks):
    """
    Generate a response using the Gemini API given a query and relevant code chunks.
    """
    # Combine retrieved chunks into context
    context = "\n\n".join(
        [f"File: {chunk['path']}\n{chunk['content']}" for chunk in retrieved_chunks]
    )

    # Create the prompt
    prompt = f"""
You are a senior software engineer analyzing a codebase.

Use ONLY the provided context to answer.

Context:
{context}

Question:
{query}

Answer clearly and technically.
"""

    # Generate text from Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Get the generated text
    return response.candidates[0].content
