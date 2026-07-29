import streamlit as st
from PIL import Image
import pytesseract
import difflib
import re

st.set_page_config(page_title="AI Paper Checker", layout="centered")

st.title("📄 AI Paper Checker")

st.write("Upload the student's answer sheet and enter the answer key.")
import streamlit as st
from PIL import Image
import pytesseract
import difflib
import re

st.set_page_config(page_title="AI Paper Checker", layout="centered")

st.title("📄 AI Paper Checker")
st.write("Upload the student's answer sheet and enter the answer key.")

answer_key = st.text_area(
    "Enter the Correct Answer Key (one answer per line)",
    height=200
)

uploaded_file = st.file_uploader(
    "Upload Student Answer Sheet",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    extracted_text = pytesseract.image_to_string(image)

    st.subheader("Extracted Text")
    st.text(extracted_text)
