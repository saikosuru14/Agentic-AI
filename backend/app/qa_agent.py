from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# pylint: disable=E0611
from langchain.chains import RetrievalQA

VECTOR_DIR = "app/vector_store/"

def answer_query(question):
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.load_local(VECTOR_DIR, embeddings)
    retriever = vectordb.as_retriever()

    llm = ChatOpenAI(model="gpt-3.5-turbo")

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa.run(question)
