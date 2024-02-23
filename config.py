# config.py

import json

with open("config.json") as config_file:
    config_data = json.load(config_file)

OPENAI_API_KEY = config_data.get("OPENAI_API_KEY")

import streamlit as st

def generate_completion(user_input):
    # This is a placeholder function for text generation
    # Replace this function with your preferred text generation method
    completed_text = user_input.upper()  # Example: Convert input to uppercase
    return completed_text

def main():
    st.title("Simple Streamlit App for Text Generation")

    # Text input field
    user_input = st.text_input("Enter some text")

    # Generate text completion
    if st.button("Generate Completion"):
        if user_input:
            completed_text = generate_completion(user_input)
            st.write("Completed Text:", completed_text)
        else:
            st.write("Please enter some text to generate completion.")

if __name__ == "__main__":
    main()
