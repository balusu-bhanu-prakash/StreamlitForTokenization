import streamlit as st
import requests

st.title("Treebank Tokenizer Demo (Flask + Streamlit)")

user_input = st.text_area("Enter text to tokenize")

if st.button("Tokenize"):
    response = requests.post(
        "http://localhost:5000/tokenize", json={"text": user_input}
    )
    if response.status_code == 200:
        tokens = response.json()["tokens"]
        st.write("### Tokens:")
        st.markdown(f"**Tokens:** {' || '.join(tokens)}")
        st.write(tokens)

    else:
        st.error("Failed to reach tokenizer API")
