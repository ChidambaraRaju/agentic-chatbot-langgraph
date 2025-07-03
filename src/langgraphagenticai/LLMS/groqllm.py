import streamlit as st
import os
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input
        
    def get_groq_llm(self):
        # Get the API key from user controls
        groq_api_key = self.user_controls_input.get("GROQ_API_KEY")
        model = self.user_controls_input.get("selected_groq_model")
        
        if not groq_api_key:
            st.error("⚠️ Please enter your GROQ API key to proceed. Don't have one? Refer to https://console.groq.com/keys")
            return None
        
        # Initialize the Groq LLM with the provided API key
        groq_llm = ChatGroq(model=model, api_key=groq_api_key)
        
        return groq_llm