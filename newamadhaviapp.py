import os
import openai
import streamlit as st
 
# Set your Azure OpenAI API key and endpoint
AZURE_OPENAI_API_KEY = "YOUR_AZURE_API_KEY"  # Replace with your actual Azure API key
AZURE_OPENAI_ENDPOINT = "https://genainorthcentralus.openai.azure.com/openai/deployments/gpt-4odeployment/chat/completions?api-version=2024-02-15-preview"  # Replace with your endpoint
AZURE_DEPLOYMENT_NAME = "gpt-4odeployment"  # Replace with your deployment name
 
# Configure OpenAI to use Azure endpoint and API key
openai.api_type = "azure"
openai.api_key = AZURE_OPENAI_API_KEY
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = ""  # Use the correct API version based on Azure's documentation
 
# Streamlit app title
st.title("Azure GPT-4 Chatbot with Streamlit")
 
# Input box for user query
user_input = st.text_input("Enter your message:")
 
# Function to generate response from Azure GPT-4
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine=AZURE_DEPLOYMENT_NAME,  # The deployment name for the model you set up in Azure
            prompt=prompt,
            max_tokens=150,  # Adjust max tokens as needed
            temperature=0.7,  # Adjust temperature for randomness
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error: {e}"
 
# Display the GPT-4 response when user input is provided
if user_input:
    response = generate_response(user_input)
    st.write(response)
