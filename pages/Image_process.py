import streamlit as st
from PIL import Image
from Input_enter import input_enter

import Retrieve_gemini_models_display as gemini_models
import Gemini_AI_Process as gemini_process 

st.set_page_config(layout="centered")

st.write("<div style='background-color:lightGreen; padding:5px; border-radius:5px;'>"
    "<h3><b>Image upload- using Google Gemini model with Python</b></h3>"
    "</div> </br> </br></br>",
    unsafe_allow_html=True)

current_page = st.query_params.get("page", ["Image"])[0]

if current_page == "Image":
  if st.button("Back to Main Page"):
    st.switch_page("LLM_GoogleGemini.py")

gemini_models.display_model_method("radio")

model_val = st.session_state.get("model_val", "")

if len(model_val) > 0 :
  uploaded_file = st.file_uploader("Upload Image", type =["png","jpg","jpeg"])
  if uploaded_file is not None:
    img = Image.open(uploaded_file)
    resized_image = img.resize((80,80))
    st.image(resized_image,caption="Uploaded Image",use_container_width=False)

  input_enter()
  prompt = st.session_state.get("prompt", "No name entered")

  st.write(f"**Name:** {prompt}")

  if st.button("GET RESPONSE"):
    img = Image.open(uploaded_file) 
    gemini_process.generate_content_basedon_image(model_val,prompt,img) 