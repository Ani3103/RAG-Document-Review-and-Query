import chromadb
import uuid
import os

# Ensure DB is persistent so it survives uvicorn restarts
db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'chroma_db')
client = chromadb.PersistentClient(path=db_path)

collection = client.get_or_create_collection(name="documents")


def store_chunks(chunks, embeddings):
    # Use UUIDs to prevent overwriting chunks from different PDFs
    ids = [str(uuid.uuid4()) for _ in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )


def search_chunks(query_embedding, top_k=5):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    if not results["documents"]:
        return []
        
    return results["documents"][0]