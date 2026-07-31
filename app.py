import streamlit as st
from PIL import Image
import difflib
import re

st.set_page_config(page_title="AI Paper Checker", layout="centered")

st.title("📄 AI Paper Checker")
st.write("Upload the student's answer sheet and enter the answer key.")

# Answer Key
answer_key = st.text_area(
    "Enter the Correct Answer Key (one answer per line)",
    height=200
)

# Upload Image
uploaded_file = st.file_uploader(
    "Upload Student Answer Sheet",
    type=["jpg", "jpeg", "png"]
)

# Student Answers
student_answers = st.text_area(
    "Enter Student Answers (one answer per line)",
    height=200
)

# Show Uploaded Image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

# Compare Answers
if answer_key.strip() != "" and student_answers.strip() != "":

    extracted_text = student_answers

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

        student_answer = student_lines[i] if i < len(student_lines) else "No Answer"

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
        st.write(f"Match: {similarity*100:.0
