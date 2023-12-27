import dotenv
dotenv.load_dotenv()

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFDirectoryLoader


# loader = DirectoryLoader('./peanut_docs/', glob="*/**.txt")
loader = PyPDFDirectoryLoader('./peanut_docs/')
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
split_docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_documents(split_docs, embeddings)
qa = RetrievalQA.from_chain_type(llm=OpenAI(), 
                                chain_type="stuff", 
                                retriever=docsearch.as_retriever(), 
                                return_source_documents=True)

import sys
while True:
    inp = input("> What you want to ask: \n")
    if inp == "q":
        print("bye")
        exit(0)

    result = qa({"query": inp})
    print(result['result'])
    print("\n")
