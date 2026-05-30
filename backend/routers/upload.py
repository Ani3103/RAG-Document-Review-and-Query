from fastapi import APIRouter, UploadFile, File
from backend.utils.pdf_parser import extract_text_from_pdf
from backend.utils.chunking import chunk_text, clean_chunks
from backend.services.embeddings import generate_embeddings
from backend.services.vectorstore import store_chunks


router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    content = await file.read()

    text = extract_text_from_pdf(content)

    from backend.utils.chunking import chunk_text, clean_chunks

    chunks = chunk_text(text)
    chunks = clean_chunks(chunks)

    embeddings = generate_embeddings(chunks)

    store_chunks(chunks, embeddings)

    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "status": "stored in vector database"
    }