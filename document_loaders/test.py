from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_mistralai import ChatMistralAI

data=TextLoader("document_Loaders/notes.txt").load()

ChatPromptTemplate.from_messages(
    [("system","you are the AI that summarizes the text "),
     ("human","{data}")]
)

model= ChatMistralAI(model="mistral-small-2506")

result=model.invoke("Hello")

print(data) 