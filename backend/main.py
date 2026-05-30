from fastapi import FastAPI
from backend.routers import upload, query, summarize, review

app = FastAPI()

app.include_router(upload.router)
app.include_router(query.router)
app.include_router(summarize.router)
app.include_router(review.router)

@app.get("/")
def root():
    return {"status": "Server running"}