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
