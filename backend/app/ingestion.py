from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os

VECTOR_DIR = "app/vector_store/"

def ingest_document(contents, filename):
    # Save the uploaded file temporarily
    file_path = os.path.join(VECTOR_DIR, filename)
    with open(file_path, 'wb') as f:
        f.write(contents)

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(docs, embeddings)
    vectordb.save_local(VECTOR_DIR)
