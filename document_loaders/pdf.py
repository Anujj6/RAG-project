from langchain_community.document_loaders import PyPDFLoader

data=pyPDFLoader("document_loaders/GRU.pdf").load()

print(data) 