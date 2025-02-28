import google.generativeai as genai

def configure_genai():
    api_key ="AIzaSyCqXNppjN4pn4ouy_LWHDYdbXXvpv7NBac"
    genai.configure(api_key=api_key)
    return genai