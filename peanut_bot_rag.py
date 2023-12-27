import dotenv
from dotenv import find_dotenv, load_dotenv 
load_dotenv(find_dotenv(), verbose=True)

import os
print("=================================")
print(os.getenv("OPENAI_API_KEY"))
print(os.getenv("X"))
print("=================================")

import bs4
from langchain import hub
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain.document_loaders import PyPDFDirectoryLoader

loader = PyPDFDirectoryLoader('./peanut_docs/')
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

import sys
while True:
    inp = input("> What you want to ask: \n")
    if inp == "q":
        print("bye")
        exit(0)

    result = rag_chain.invoke(inp)
    print(result)
    print("\n")





