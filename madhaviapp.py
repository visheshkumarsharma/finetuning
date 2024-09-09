import openai
import streamlit as st
 
# Set OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual OpenAI API key
 
# Streamlit app title
st.title("GPT-4 Chatbot with Streamlit")
 
# Input box for user query
user_input = st.text_input("Enter your message:")
 
# Function to generate response from GPT-4
def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,  # Adjust max tokens as needed
            temperature=0.7,  # Adjust temperature for randomness
        )
        message = response['choices'][0]['message']['content']
        return message.strip()
    except Exception as e:
        return f"Error: {e}"
 
# Display the GPT-4 response when user input is provided
if user_input:
    response = generate_response(user_input)
    st.write(response)
