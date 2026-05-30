from sentence_transformers import SentenceTransformer

# load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(text_chunks):
    embeddings = model.encode(text_chunks)
    return embeddings.tolist()


def embed_query(query):
    embedding = model.encode([query])
    return embedding.tolist()[0]