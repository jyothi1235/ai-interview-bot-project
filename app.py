# app.py

import streamlit as st
from utils import extract_text, generate_questions, evaluate_answer, get_ideal_answer

st.set_page_config(page_title="AI Interview Bot")

st.title("🤖 AI Interview Bot (Enterprise Version)")

# Upload Resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text(uploaded_file)

    st.subheader("Generated Interview Questions")
    questions = generate_questions(text)

    user_answers = []

    for i, q in enumerate(questions):
        ans = st.text_area(f"Q{i+1}: {q}")
        user_answers.append(ans)

    if st.button("Evaluate Answers"):

        total_score = 0

        for i in range(len(questions)):
            ideal = get_ideal_answer(questions[i])
            score = evaluate_answer(user_answers[i], ideal)

            total_score += score

            st.write(f"### Q{i+1} Score: {round(score*10,2)}/10")

            if score > 0.7:
                st.success("Good Answer")
            elif score > 0.4:
                st.warning("Average Answer")
            else:
                st.error("Poor Answer")

        final = (total_score / len(questions)) * 10
        st.subheader(f"Final Score: {round(final,2)}/10")