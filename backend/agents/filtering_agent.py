import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


def filter_relevant_context(question, chunks):
    if not chunks:
        return ""

    context = "\n\n".join(chunks)
    model = genai.GenerativeModel('gemini-flash-lite-latest')

    prompt = f"""
    You are an AI system that filters relevant information.

    Question:
    {question}

    Context:
    {context}

    Task:
    Extract ONLY the parts of the context that are directly useful to answer the question.

    Remove:
    - irrelevant information
    - introductions
    - metadata

    Keep it concise.
    """

    response = model.generate_content(prompt)
    try:
        return response.text.strip()
    except ValueError:
        return ""
