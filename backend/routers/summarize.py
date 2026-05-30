from fastapi import APIRouter

router = APIRouter()

@router.post("/summarize")
def summarize():
    return {"message": "Summarizer placeholder"}
