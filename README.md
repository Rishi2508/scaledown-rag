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
