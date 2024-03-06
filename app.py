import streamlit as st

name = st.text_input("あなたの名前を入力してください")
st.write("こんにちは、", name)