import streamlit as st
import Connect_with_geminAI_using_APIkey as genai_connect

st.set_page_config(layout="centered")

st.write("<div style='background-color:lightiink; padding:5px; border-radius:5px;'>"
    "<h1><b>LLM - Google Gemini Model with Python</b></h1>"
    "</div> </br> </br></br>",
    unsafe_allow_html=True)
    
current_page = st.query_params.get("page", ["main"])[0]
genai_connect = genai_connect.configure_genai()

if st.button("Image Upload"):
    st.switch_page("pages\Image_process.py")        
if st.button("Text Chat"):
    st.switch_page("pages\Text_process.py")