import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatIP(dimension)
        self.documents = []

    def add(self, embeddings, documents):
        embeddings = np.array(embeddings).astype("float32")

        # Normalize embeddings for cosine similarity
        faiss.normalize_L2(embeddings)

        self.index.add(embeddings)
        self.documents.extend(documents)

    def search(self, query_embedding, k=3):
        query_embedding = np.array([query_embedding]).astype("float32")

        # Normalize query
        faiss.normalize_L2(query_embedding)

        distances, indices = self.index.search(query_embedding, k)

        results = []
        for i in indices[0]:
            if i < len(self.documents):
                results.append(self.documents[i])

        return results
