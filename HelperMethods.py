import streamlit as st
def select_model_name(models):
  cleaned_models = [m.name.replace("models/", "") for m in models]
  models_1_5 = [model for model in cleaned_models if "gemini-1.5" in model]
  models_2_0 = [model for model in cleaned_models if "gemini-2.0" in model]
  return models_1_5, models_2_0

# Function to update URL parameters (navigate to a new page)
def navigate_to(page_name):
    st.query_params.get("page",page_name)[0]
    st.rerun()  # Rerun the app to update UI