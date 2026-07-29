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
if uploaded_file is not None and answer_key.strip() != "":

    key_lines = [line.strip() for line in answer_key.split("\n") if line.strip()]
    student_lines = [line.strip() for line in extracted_text.split("\n") if line.strip()]

    total_questions = len(key_lines)
    correct_answers = 0

    st.subheader("Result")

    for i in range(total_questions):

        key_answer = re.sub(
            r'^Q\d+[:.]?\s*',
            '',
            key_lines[i],
            flags=re.IGNORECASE
        ).strip()

        if i < len(student_lines):
            student_answer = student_lines[i]
        else:
            student_answer = "No Answer"

        similarity = difflib.SequenceMatcher(
            None,
            key_answer.lower(),
            student_answer.lower()
        ).ratio()

        if similarity >= 0.70:
            st.success(f"Question {i+1}: Correct")
            correct_answers += 1
        else:
            st.error(f"Question {i+1}: Wrong")

        st.write("Correct Answer:", key_answer)
        st.write("Student Answer:", student_answer)
        st.write(f"Match: {similarity*100:.0f}%")
        st.write("---")

    percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

    st.header("Final Score")
    st.success(f"Marks: {correct_answers}/{total_questions}")
    st.info(f"Percentage: {percentage:.2f}%")
