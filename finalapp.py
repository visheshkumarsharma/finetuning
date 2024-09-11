import os
import requests
import base64
import streamlit as st
import pandas as pd
 
# Configuration
API_KEY = "b5d5b5ea2ebd471b88b631a34ab7d522"
st.title("ATE TEST CODE GENERATION")
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}
 
# Payload for the request
payload = {
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "code for the given requirement in cpp for the pin configuration test case using PS instrument,force all pins to 0V and then Force -0.010 mA to the pin under test LED2 and measure the voltage (MV)"
        }
      ]
    }
  ],
  "temperature": 0.0,
  "top_p": 0.95,
  "max_tokens": 800
}
 
ENDPOINT = "https://genainorthcentralus.openai.azure.com/openai/deployments/gpt-4odeployment/chat/completions?api-version=2024-02-15-preview"
 
# Send request
try:
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")
 
# Handle the response as needed (e.g., print or process)
content=response.text
content=list(content)
print(content)
print(type(content))
st.write(content)
