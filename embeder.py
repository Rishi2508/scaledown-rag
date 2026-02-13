from sentence_transformers import SentenceTransformer

# Load model once (global)
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    return model.encode(texts, show_progress_bar=True, normalize_embeddings=True)


def embed_query(query):
    return model.encode(query, normalize_embeddings=True)
