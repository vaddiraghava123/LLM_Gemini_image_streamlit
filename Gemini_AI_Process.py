import streamlit as st
import google.generativeai as genai

   
def generate_content_basedon_image(model_name, prompt, img):
    model = genai.GenerativeModel(model_name)
    response = model.generate_content([prompt,img])
    st.markdown(response.text)

def generate_content_basedon_text(model_name, prompt):
    model = genai.GenerativeModel(model_name)
    chat = model.start_chat(history=[])
    if not chat.history:
        response =chat.send_message(prompt, stream=False)
        st.markdown(response.text)
    
class Switch:
    def __init__(self, val):
        self.val = val
        self.flag = False
    
    def case_method(self, condition, action):
        if not self.flag and self.val == condition:
            action()
            self.flag = True
    
    def default_method(self, action):
        if not self.flag:
            action()   


def switch_method(val):
    switch = Switch(val)
    switch.case_method("Image", lambda : generate_content_basedon_image())
    switch.case_method("Text", lambda : generate_content_basedon_text())
    switch.default_method(lambda: generate_content_basedon_image())