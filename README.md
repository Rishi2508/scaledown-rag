Scaledown RAG (v1.1)

A lightweight Retrieval-Augmented Generation (RAG) system for semantic codebase search.

This project indexes Python source code using embeddings and performs similarity search to retrieve relevant code snippets based on natural language queries.

What’s New in v1.1

Version 1.1 introduces major architectural improvements:

 File chunking (instead of full-file embeddings)
 Chunk-level embeddings
 Snippet-level retrieval
 Improved search precision
 Cleaner indexing pipeline

This makes the system behave like a real RAG engine instead of a simple file matcher.
<<<<<<< HEAD
Here’s a concise and clear README update for v1.3 of your RAG project:

Scaledown RAG System v1.3

Version: 1.3
Date: 2026-02-13

Overview

This version (v1.3) enhances the Retrieval-Augmented Generation (RAG) system for analyzing Python codebases. It integrates Google Gemini 2.5 for text generation, enabling more accurate and context-aware code explanations.

New Features in v1.3

Gemini API Integration

Replaced deprecated google.generativeai with google.genai.

Uses genai.Client and models.generate_content for generating responses.

Improved Codebase Analysis

Handles Python files with enhanced chunking and vector indexing.

Produces clear, technically detailed answers from retrieved code chunks.

Environment Variable Support

Supports GEMINI_API_KEY and GOOGLE_API_KEY.

Automatically picks the correct key when both are present.

Stable RAG Pipeline

Loads embeddings with sentence-transformers/all-MiniLM-L6-v2.

Uses VectorStore for efficient similarity search.

Handles user queries interactively, generating accurate code explanations.
🧠 Codebase RAG Assistant

An intelligent Retrieval-Augmented Generation (RAG) system that allows you to upload a Python project and ask questions about the codebase.

It analyzes source files, builds embeddings, and generates contextual answers with source references.

🚀 Features

📂 Upload a Python project (ZIP)

🧩 Smart code chunking

🧠 Embedding-based semantic search

🔎 Top-K relevant code retrieval

💬 Natural language answers

🏷️ Function name tagging

🗂️ Source file tracking

🧠 Temporary chat history memory

🌐 Simple and clean frontend

🏗️ Architecture Overview
Frontend (HTML)
        ↓
Flask Server (server.py)
        ↓
RAG Service (rag_service.py)
        ↓
---------------------------------
Loader → Chunker → Embedder
        ↓
Vector Store (FAISS-like)
        ↓
Generator (LLM)
---------------------------------

📁 Project Structure
rag/
│
├── server.py              # Flask backend
├── rag_service.py         # Core RAG logic
├── loader.py              # Loads Python files
├── chunker.py             # Splits code into chunks
├── embeder.py             # Creates embeddings
├── vectorstore.py         # Vector index handling
├── generator.py           # Answer generation
├── ast_parser.py          # Function extraction/tagging
├── zip_handler.py         # ZIP extraction
│
├── templates/
│   └── index.html         # Frontend UI
│
└── uploads/               # Temporary project storage

⚙️ Installation
1️⃣ Clone the repository
git clone <your-repo-url>
cd rag

2️⃣ Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the Application
python server.py


Then open:

http://127.0.0.1:5000

🧪 How It Works

Upload a Python project (.zip)

Files are loaded and chunked

Embeddings are generated

Vector index is built

Ask questions about the codebase

System retrieves relevant chunks

LLM generates contextual answer

🧠 Example Questions

"What does test.py do?"

"Where is authentication handled?"

"Explain the build_index function."

"How are embeddings generated?"

"Which file handles user uploads?"

🛠️ Tech Stack

Python

Flask

Vector Search (FAISS-style implementation)

Embedding Model

LLM for Answer Generation

HTML / CSS / JS frontend

📌 Current Capabilities

Temporary in-memory vector index

Single-user usage

Session-based chat memory

Function-level tagging via AST

🔮 Future Improvements

Persistent vector storage

Multi-user support

Streaming answers

Improved ranking

Docker deployment

GitHub integration

Production deployment

🧑‍💻 Author

Built as a learning + development project to understand:

RAG architecture

Code intelligence systems

Embedding pipelines

LLM-based QA systems

📜 License

This project is for educational and development purposes.

