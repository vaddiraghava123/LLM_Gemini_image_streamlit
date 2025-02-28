import streamlit as st
import google.generativeai as genai
import HelperMethods as helper

def retrieve_gemini_models():    
    model_1_5 , model_2_0 = helper.select_model_name(genai.list_models())
    return model_1_5 , model_2_0


def display_selected_drop_down_gemini_model():
    model = st.selectbox("Select a Gemini Model", ["None", "Gemini 1.5", "Gemini 2.0"])    
    selected_option_2_0 =""
    selected_option_1_5 = ""    
    model_1_5, model_2_0 = retrieve_gemini_models()
    if model == "Gemini 1.5":
        selected_option_1_5 = st.selectbox("Select an option:", model_1_5)
        display_selected_model("select",selected_option_1_5)
    elif model == "Gemini 2.0":
        selected_option_2_0= st.selectbox("Select an option:", model_2_0)  
        display_selected_model("select",selected_option_2_0)
    else:
        st.write("Please select any model")  
    

def display_radio_buttons_gemini_model():
    # Radio Buttons
    model = st.selectbox("Select a Gemini Model", ["None", "Gemini 1.5", "Gemini 2.0"])    
    selected_radio_1_5 = ""
    selected_radio_2_0 = ""
    model_1_5, model_2_0 = retrieve_gemini_models()
    if model == "Gemini 1.5":
        selected_radio_1_5 = st.radio("Choose an option:", model_1_5)
        display_selected_model("radio",selected_radio_1_5)
    elif model == "Gemini 2.0":
        selected_radio_2_0 = st.radio("Choose an option:", model_2_0)
        display_selected_model("select",selected_radio_2_0)
    else:
        st.write("Please select any model")

    
def display_checkbox_gemini_model():
    model = st.selectbox("Select a Gemini Model", ["None", "Gemini 1.5", "Gemini 2.0"])  
    selected_checkbox_1_5 = ""
    selected_checkbox_2_0 = ""
    model_1_5, model_2_0 = retrieve_gemini_models()
    if model == "Gemini 1.5":
        selected_checkbox_1_5 = [model for model in model_1_5 if st.checkbox(model, key=model)]
        display_selected_model("checkbox",selected_checkbox_1_5)
    elif model == "Gemini 2.0":
        selected_checkbox_2_0 = [model for model in model_2_0 if st.checkbox(model, key=model)]
        display_selected_model("checkbox",selected_checkbox_2_0)
    else:
        st.write("Please select any model")

def display_selected_model(model_type, model_val) :
    st.subheader("Selected Models")
    st.write("You ", {model_type},": ", model_val if len(model_val) > 0 else "")
    if model_type=='checkbox':
        st.write("You : checkbox", model_val[0] if len(model_val) > 0 else "")
    st.session_state["model_val"] = model_val

    
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


def display_model_method(val):
    switch = Switch(val)
    switch.case_method("select", lambda : display_selected_drop_down_gemini_model())
    switch.case_method("radio", lambda : display_radio_buttons_gemini_model())
    switch.case_method("checkbox", lambda : display_checkbox_gemini_model())
    switch.default_method(lambda: display_radio_buttons_gemini_model())
