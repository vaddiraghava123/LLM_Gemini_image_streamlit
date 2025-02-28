import streamlit as st
import google.generativeai as genai

from Input_enter import input_enter 
import Retrieve_gemini_models_display as gemini_models
import Gemini_AI_Process as gemini_process 

st.set_page_config(layout="wide")

st.write("<div style='background-color:lightblue; padding:5px; border-radius:5px;'>"
    "<h3><b>Chat Text - using Google Gemini model with Python</b></h3>"
    "</div> </br> </br></br>",
    unsafe_allow_html=True)

current_page = st.query_params.get("page", ["Text"])[0]

if current_page == "Text":
  if st.button("Back to Main Page"):
    st.switch_page("LLM_GoogleGemini.py")
    
gemini_models.display_model_method("select")

model_val = st.session_state.get("model_val", "")

if len(model_val) > 0 :
  input_enter()
  prompt = st.session_state.get("prompt", "No name entered")
  st.write(f"**Name:** {prompt}")

  if st.button("GET RESPONSE"):
    models = str(model_val)
    gemini_process.generate_content_basedon_text(models,prompt )