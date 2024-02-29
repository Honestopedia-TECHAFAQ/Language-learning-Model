import streamlit as st
import requests

def query_model(prompt):
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json',
    }
    data = {
        'prompt': prompt,
        'max_tokens': 50,
    }
    response = requests.post('https://api.openai.com/v1/engines/text-davinci-002/completions', headers=headers, json=data)
    return response.json()

st.title("Language Learning Model")

user_input = st.text_area("Enter your prompt:")

if st.button("Generate Response"):
    model_response = query_model(user_input)
    
    if 'choices' in model_response and len(model_response['choices']) > 0:
        st.text("Model Response:")
        st.write(model_response['choices'][0]['text'])
    else:
        st.text("Error: Unable to generate response")
