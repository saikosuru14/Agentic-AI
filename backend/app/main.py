from fastapi import FastAPI, UploadFile, File
from ingestion import ingest_document
from qa_agent import answer_query

app = FastAPI()

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    contents = await file.read()
    filename = file.filename
    ingest_document(contents, filename)
    return {"message": f"{filename} uploaded and ingested."}

@app.get("/query/")
async def query_doc(question: str):
    answer = answer_query(question)
    return {"answer": answer}
