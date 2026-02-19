from loader import load_python_files
from embeder import embed_texts, embed_query
from vectorstore import VectorStore
from generator import generate_answer
from ast_parser import parse_code

# -----------------------------
# Global State (Single User App)
# -----------------------------
store = None
documents = None
chat_history = []   # 🔥 Temporary memory


# -----------------------------
# Build Index
# -----------------------------
def build_index(project_path):
    global store, documents, chat_history

    print("🔄 Building index...")
    chat_history = []  # Reset memory when new project uploaded

    files = load_python_files(project_path)
    print(f"📂 Files loaded: {len(files)}")

    if not files:
        raise ValueError("No Python files found.")

    chunks = []

    for file in files:
        file_path = file["path"]
        content = file["content"]

        try:
            ast_chunks = parse_code(content)
        except Exception as e:
            print(f"⚠️ AST failed for {file_path}: {str(e)}")
            continue

        for chunk in ast_chunks:
            chunk["path"] = file_path
            chunk["length"] = len(chunk["content"])
            chunks.append(chunk)

    print(f"✂️ AST Chunks created: {len(chunks)}")

    if not chunks:
        print("⚠️ No AST chunks found. Falling back to full file chunking.")
    for file in files:
        chunks.append({
            "type": "file",
            "name": file["path"],
            "content": file["content"],
            "path": file["path"],
            "length": len(file["content"])
        })
    chunk_texts = [
        f"{c['type']} {c['name']} in {c['path']}:\n{c['content']}"
        for c in chunks
    ]

    chunk_embeddings = embed_texts(chunk_texts)

    dimension = len(chunk_embeddings[0])
    store = VectorStore(dimension)

    store.add(chunk_embeddings, chunks)
    documents = chunks

    print("✅ Index built successfully.")


# -----------------------------
# Answer Query
# -----------------------------
def answer_query(question, top_k=3):
    global store, chat_history

    if store is None:
        raise ValueError("Index not built.")

    if not question.strip():
        return {"answer": "Question cannot be empty.", "sources": []}

    # 🔥 Add history context
    history_text = ""
    for entry in chat_history[-3:]:  # last 3 messages
        history_text += f"User: {entry['question']}\nAssistant: {entry['answer']}\n"

    contextual_query = history_text + "\nCurrent Question: " + question

    # Embed
    query_embedding = embed_query(contextual_query)

    # Retrieve
    top_chunks = store.search(query_embedding, k=top_k)

    if not top_chunks:
        return {"answer": "No relevant code found.", "sources": []}

    # Generate answer
    answer = generate_answer(contextual_query, top_chunks)

    # Save to memory
    chat_history.append({
        "question": question,
        "answer": answer
    })

    sources = list({chunk["path"] for chunk in top_chunks})

    return {
        "answer": answer,
        "sources": sources,
        "retrieved_chunks": top_chunks
    }
