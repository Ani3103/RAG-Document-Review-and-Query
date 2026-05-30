from fastapi import APIRouter
from backend.agents.retrieval_agent import retrieve_relevant_chunks
from backend.agents.filtering_agent import filter_relevant_context
from backend.agents.reasoning_agent import generate_answer

router = APIRouter()


@router.post("/ask")
def ask_question(question: str):
    try:
        chunks = retrieve_relevant_chunks(question)
        
        if not chunks:
            return {
                "question": question,
                "answer": "⚠️ Error: No document is currently loaded in the system! Please go to the sidebar, upload a PDF, and make sure to click the **'Process Document'** button before asking a question."
            }

        # Bypass filtering_agent since Gemini handles large context well and filtering might be too aggressive
        context = "\n\n".join(chunks)
        
        answer = generate_answer(question, context)

        return {
            "question": question,
            "answer": answer
        }
    except Exception as e:
        import traceback
        return {
            "question": question,
            "answer": f"Backend Error: {str(e)}\n{traceback.format_exc()}"
        }