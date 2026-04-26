# utils.py

import re
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract text from PDF
def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# Generate simple questions from resume
def generate_questions(text):
    questions = []

    if "python" in text.lower():
        questions.append("Explain Python and its use cases.")

    if "machine learning" in text.lower():
        questions.append("What is Machine Learning? Explain types.")

    if "deep learning" in text.lower():
        questions.append("What is Deep Learning?")

    if "project" in text.lower():
        questions.append("Explain one of your projects.")

    if len(questions) == 0:
        questions = [
            "Tell me about yourself.",
            "What are your strengths?"
        ]

    return questions


# Evaluate answer
def evaluate_answer(user, ideal):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([user, ideal])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return similarity


# Ideal answers (basic)
def get_ideal_answer(question):
    if "python" in question.lower():
        return "Python is a programming language used for data science, web development and automation."

    if "machine learning" in question.lower():
        return "Machine learning is a subset of AI that learns from data."

    if "deep learning" in question.lower():
        return "Deep learning is a subset of machine learning using neural networks."

    if "project" in question.lower():
        return "Explain problem, approach, and results of project."

    return "General answer explaining the concept."