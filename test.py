# generator.py
from google import genai
import os

# Read API key from environment
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set!")

# Create Gemini client
client = genai.Client(api_key=api_key)

def generate_answer(query, retrieved_chunks):
    """
    Generate a response using Gemini API given a query and relevant code chunks.
    """
    # Combine chunks into context
    context = "\n\n".join(
        [f"File: {chunk['path']}\n{chunk['content']}" for chunk in retrieved_chunks]
    )

    # Prompt
    prompt = f"""
You are a senior software engineer analyzing a codebase.

Use ONLY the provided context to answer.

Context:
{context}

Question:
{query}

Answer clearly and technically.
"""

    # Use the new SDK interface
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
