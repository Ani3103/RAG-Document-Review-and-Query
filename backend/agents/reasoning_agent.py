import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


def generate_answer(question, context):
    try:
        model = genai.GenerativeModel('gemini-flash-lite-latest')

        prompt = f"""
You are an AI assistant analyzing a document to answer a user's question.

Question:
{question}

Document Context:
{context}

Instructions:
1. Answer the question based ONLY on the provided Document Context.
2. If the context does not contain the answer, explicitly state: "The uploaded document does not contain information to answer this question."
3. Do NOT hallucinate or add outside knowledge.
4. Keep the answer concise and well-formatted. Use bullet points only if there are multiple parts.
"""

        response = model.generate_content(prompt)
        try:
            return response.text.strip()
        except ValueError:
            return "No information could be generated."

    except Exception as e:
        return f"Error: {str(e)}"
