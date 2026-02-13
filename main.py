from loader import load_python_files
from embeder import embed_texts, embed_query
from vectorstore import VectorStore
from chunker import chunk_text
from generator import generate_answer


def main():
    print("Loading codebase...\n")
    docs = load_python_files("../../scaledown")  # Update path if needed

    if not docs:
        print("No Python files found.")
        return

    print(f"Loaded {len(docs)} files.\n")

    print("Chunking documents...\n")
    all_chunks = []
    chunk_metadata = []

    for doc in docs:
        chunks = chunk_text(doc["content"])
        for chunk in chunks:
            all_chunks.append(chunk)
            chunk_metadata.append({
                "path": doc["path"],
                "content": chunk
            })

    print(f"Generated {len(all_chunks)} chunks.\n")

    print("Generating embeddings...\n")
    embeddings = embed_texts(all_chunks)

    print("Creating vector index...\n")
    store = VectorStore(len(embeddings[0]))
    store.add(embeddings, chunk_metadata)

    print("RAG System v1.3 Ready.\n")

    while True:
        query = input("Ask about the codebase (or type 'exit'): ")
        if query.lower() == "exit":
            break

        print("\nSearching...\n")
        query_embedding = embed_query(query)
        results = store.search(query_embedding)

        if not results:
            print("No relevant chunks found.\n")
            continue

        print("\nGenerating answer...\n")
        answer = generate_answer(query, results)
        print(answer)
        print("-" * 80)


if __name__ == "__main__":
    main()
