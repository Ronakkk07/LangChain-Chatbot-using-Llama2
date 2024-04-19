from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama 
# from dotenv import load_dotenv

# load_dotenv()

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server",
)

add_routes(
    app, 
    Ollama(),
    path = "/ollama"
)
llm = Ollama(model = "llama2")

prompt1 = ChatPromptTemplate.from_template("{topic} with 200 words")

add_routes(
    app,
    prompt1| llm,
    path = "/essay"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

# APIs Created
    