import os
import requests
import base64
import streamlit as st
 
# Configuration
API_KEY = "b5d5b5ea2ebd471b88b631a34ab7d522"
st.write("GPT4o CODE GENERATED")
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
          "text": "generate c++ code using PS instrument, force all pins to 0V and then Force -0.010 mA to the pin under test LED2 and measure the voltage (MV)"
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
content=response.json()
st.write(content)
