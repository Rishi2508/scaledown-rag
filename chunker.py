def chunk_code(documents, chunk_size=800, overlap=100):
    chunks = []

    for doc in documents:
        content = doc["content"]
        path = doc["path"]

        start = 0
        while start < len(content):
            end = start + chunk_size
            chunk_text = content[start:end]

            chunks.append({
                "path": path,
                "content": chunk_text
            })

            start += chunk_size - overlap

    return chunks
