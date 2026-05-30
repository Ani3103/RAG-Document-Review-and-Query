import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


def rewrite_query(query: str):

    model = genai.GenerativeModel('gemini-flash-lite-latest')

    prompt = f"""
    Rewrite the following query to improve semantic search.
    Focus on expanding intent and key concepts.

    Query: {query}
    """

    response = model.generate_content(prompt)
    try:
        return response.text.strip()
    except ValueError:
        return query # Fallback to original query if rewriting fails
