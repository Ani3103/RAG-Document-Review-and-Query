from backend.services.embeddings import embed_query
from backend.services.vectorstore import search_chunks
from backend.agents.query_agent import rewrite_query


def retrieve_relevant_chunks(query: str, top_k: int = 8):

    improved_query = rewrite_query(query)

    query_embedding = embed_query(improved_query)

    results = search_chunks(query_embedding, top_k)

    return results