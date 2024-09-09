import openai
import streamlit as st
import pandas as pd
from googletrans import Translator
import re
import string
 
# Function to convert each row in the dataframe
def convert(row):
    s = row['Pin of Interest']
    v = row[s]
    return f"Force {v} on {s} pin and measure the voltage on the same {s} pin with SPU with range of {row['Lower Limit']} and {row['Upper Limit']}."
 
# Function to clean text
def clean_text(text):
    printable_text = ''.join(char for char in text if char in string.printable)  # Remove non-printable characters
    cleaned_text = re.sub(r'[^\x00-\x7F]', '', printable_text)  # Remove non-ASCII characters
    return cleaned_text
 
# Function to translate text to English
def translate_to_english(text, src_lang='auto'):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest='en')
    return translation.text
 
# Initialize OpenAI client
openai.api_key = "api_key"  # Replace with your Azure OpenAI or OpenAI API key
 
def process_client(model_name, df):
    x = ""
    options = df['english sentence'].tolist()
    z = st.radio('Select a sentence:', options)
    if z:
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[{"role": "user", "content": z}],
            max_tokens=500,
            stream=True
        )
        for message in response:
            x += message.choices[0].delta.content
 
    return x
 
def main():
    st.set_page_config(layout="wide", page_title="MODELS")
    image_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfM34DG2u5fZI_pslFvrMpPKNNRBtbknBlVg&s"
    st.sidebar.image(image_URL, use_column_width=True)
    # Sidebar UI for uploading file and selecting model
    st.title("ATE TEST CODE GENERATION")
    st.sidebar.title("Model Selection and File Upload")
    uploaded_f = st.sidebar.file_uploader("Upload your Excel file", type=["csv"])
    selected_model = st.sidebar.selectbox("Choose your model", options=["gpt-4"])  # Add more models as needed
 
    if uploaded_f is not None:
        try:
            df = pd.read_csv(uploaded_f)
            # Display original dataframe
            st.subheader("Original Test Case File")
            st.dataframe(df)
 
            # Convert dataframe to English sentences
            df['english sentence'] = df.apply(convert, axis=1)
 
            # Display dataframe with English conversion
            st.subheader("Dataframe with English Conversion")
            st.dataframe(df['english sentence'])
 
            # Add prefix to English sentences
            promtg = "code for the given requirement using customlibrary in cpp for the pin configuration test case"
            df['english sentence'] = df['english sentence'].apply(lambda x: promtg + x)
 
            # Process selected model
            if selected_model:
                st.subheader(f"Interact with {selected_model} Model")
                x = process_client(selected_model, df)
            else:
                st.warning(f"Model {selected_model} is not configured or available.")
 
            # Translate and clean the final output
            x = translate_to_english(x)
            x = clean_text(x)
 
            # Display final translated and cleaned output
            st.subheader("Final Translated and Cleaned Output")
            st.write(x)
 
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
 
if __name__ == '__main__':
    main()
