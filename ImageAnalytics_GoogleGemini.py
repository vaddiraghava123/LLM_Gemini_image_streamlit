import streamlit as st
import google.generativeai as genai
from PIL import Image

api_key ="AIzaSyCqXNppjN4pn4ouy_LWHDYdbXXvpv7NBac"
genai.configure(api_key=api_key)
st.set_page_config(layout="wide")
st.title("Image - analytics using Google Gemini model with Python")

uploaded_file = st.file_uploader("Upload Image", type =["png","jpg","jpeg"])
if uploaded_file is not None:
  img = Image.open(uploaded_file)
  resized_image = img.resize((80,80))
  st.image(resized_image,caption="Uploaded Image",use_container_width=False)


prompt = st.text_input("Enter the text ")

if st.button("GET RESPONSE"):
  img = Image.open(uploaded_file)    
  model = genai.GenerativeModel("gemini-1.5-flash")
  response = model.generate_content([prompt,img])
  st.markdown(response.text)
