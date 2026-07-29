import streamlit as st
from PIL import Image
import pytesseract
import difflib
import re

st.set_page_config(page_title="AI Paper Checker", layout="centered")

st.title("📄 AI Paper Checker")

st.write("Upload the student's answer sheet and enter the answer key.")
