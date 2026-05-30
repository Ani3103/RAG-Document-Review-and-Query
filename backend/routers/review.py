from fastapi import APIRouter
from backend.services.vectorstore import collection
from backend.agents.review_agent import generate_review_report

router = APIRouter()

@router.post("/review")
def review_document():
    # Retrieve all chunks from the vector store
    result = collection.get()
    chunks = result.get("documents", [])
    
    if not chunks:
        return {"review_report": "No document found. Please upload a PDF first."}
    
    # Combine chunks to form the context.
    # Note: To avoid exceeding the context limit of 'phi' (2048 tokens), 
    # we limit the context to a certain number of characters or chunks.
    # For MVP, we take the first 3000 characters (approx 700 tokens).
    
    combined_text = "\n".join(chunks)
    context = combined_text[:3000] 
    
    report = generate_review_report(context)
    
    return {
        "review_report": report
    }
