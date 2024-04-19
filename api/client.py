import requests
import streamlit as st 

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", json={'input': {'topic': input_text}})

    return response.json()['output']

st.title('Langchain|Langserve Demo with Llama2')
input_text = st.text_input("Know more about the topic you love.So, what would you like to know about?")

if input_text:
    st.write(get_ollama_response(input_text))

# Application interacting with api