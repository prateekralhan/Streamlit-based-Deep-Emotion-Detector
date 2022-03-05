from transformers import pipeline
import streamlit as st
from PIL import Image
import os
from app_funcs import *


st.set_page_config(
    page_title="Emotion Detector",
    page_icon="😉",
    layout="centered",
    initial_sidebar_state="auto",
)

top_image = Image.open('static/banner_top.png')
bottom_image = Image.open('static/banner_bottom.png')
main_image = Image.open('static/main_banner.png')

upload_path = "uploads/"
download_path = "downloads/"

st.sidebar.image(top_image,use_column_width='auto')
format_type = st.sidebar.selectbox('Detect Emotion from? 😯',["Plain Text 📝","Documents 📑"])
st.sidebar.image(bottom_image,use_column_width='auto')

st.image(main_image,use_column_width='auto')
st.title("😲 Deep Emotion Detector 😄")

if format_type == "Plain Text 📝":
    text = st.text_area("Enter your text here: 🎯", height=300)

    if st.button("Find Emotion ✨") and (text or len(text) != 0):
        with st.spinner(f"Finding Emotion... 💫"):
            emotion_output = emotion_generate(text)
        if emotion_output:
            st.success("✅ " + emotion_output.title())
            download_success()
    else:
        st.warning("Please enter the text and choose \"Find Emotion ✨\"")

if format_type == "Documents 📑":
    st.info('Supports all popular document formats 📄 - TXT, PDF, DOCX 😉')
    uploaded_file = st.file_uploader("Upload Document 📃", type=["txt","pdf","docx"])
    if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())
        if uploaded_file.name.endswith('.txt') or uploaded_file.name.endswith('.TXT'):
            with st.spinner(f"Finding Emotion... 💫"):
                uploaded_txt_file = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                downloaded_txt_file = os.path.abspath(os.path.join(download_path,str("processed_"+uploaded_file.name)))
                text = extract_text_txt(uploaded_txt_file,downloaded_txt_file)
                emotion_output = emotion_generate(text)
            if emotion_output and len(emotion_output) != 0:
                st.success("✅ " + emotion_output.title())
                download_success()

        if uploaded_file.name.endswith('.pdf') or uploaded_file.name.endswith('.PDF'):
            with st.spinner(f"Finding Emotion... 💫"):
                uploaded_pdf_file = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                text = extract_text_pdf(uploaded_pdf_file)
                emotion_output = emotion_generate(text)
            if emotion_output and len(emotion_output) != 0:
                st.success("✅ " + emotion_output.title())
                download_success()

        if uploaded_file.name.endswith('.docx') or uploaded_file.name.endswith('.DOCX'):
            with st.spinner(f"Finding Emotion... 💫"):
                uploaded_docx_file = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                text = extract_text_docx(uploaded_docx_file)
                emotion_output = emotion_generate(text)
            if emotion_output and len(emotion_output) != 0:
                st.success("✅ " + emotion_output.title())
                download_success()

    else:
        st.warning('⚠ Please upload your document 😯')


st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Deep Emotion Detector WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)
