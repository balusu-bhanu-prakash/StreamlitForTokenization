import streamlit as st
from tokenizer import tokenize_text  # Direct import

st.title("Text Tokenization App")

user_input = st.text_area("Enter your text here:")

if st.button("Tokenize"):
    if user_input.strip():
        tokens = tokenize_text(user_input)
        st.markdown(f"**Tokens:** {' || '.join(tokens)}")
        st.write(tokens)  # Output without indices
    else:
        st.warning("Please enter some text.")
