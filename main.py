from loader import load_python_files
from embeder import embed_texts, embed_query
from vectorstore import VectorStore


def main():
    print("Loading codebase...\n")

    # Change this path if needed
    docs = load_python_files("../../scaledown")

    if not docs:
        print("No Python files found.")
        return

    print(f"Loaded {len(docs)} files.\n")

    texts = [doc["content"] for doc in docs]

    print("Generating embeddings...\n")
    embeddings = embed_texts(texts)

    print("Creating vector index...\n")
    store = VectorStore(len(embeddings[0]))
    store.add(embeddings, docs)

    print("RAG System Ready.\n")

    while True:
        query = input("Ask about the codebase (or type 'exit'): ")

        if query.lower() == "exit":
            break

        query_embedding = embed_query(query)
        results = store.search(query_embedding)

        print("\nTop Matches:\n")

        for r in results:
            print("File:", r["path"])
            print("-" * 60)


if __name__ == "__main__":
    main()
