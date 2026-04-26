# 🤖 AI Interview Bot

## 📌 Overview

The **AI Interview Bot** is a machine learning-based application that simulates a basic interview process. It generates interview questions, collects user responses, and evaluates answers to provide a score and feedback.

This project demonstrates how Natural Language Processing (NLP) techniques can be used to build simple AI-driven evaluation systems. Many modern interview bots follow similar workflows of generating questions and evaluating responses automatically ([Streamlit][1]).

---

## 🚀 Live Demo

👉 Try the application here:
🔗 https://jyothi1235-ai-interview-bot-project-app-nmtsdc.streamlit.app/

---

## 🎯 Features

* Generate interview questions based on input
* Accept user answers through an interactive interface
* Evaluate answers using similarity techniques (TF-IDF)
* Provide score and feedback
* Simple and user-friendly UI using Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Scikit-learn**
* **NLP (TF-IDF, Cosine Similarity)**

---

## ⚙️ How It Works

1. User inputs or uploads content
2. System generates relevant interview questions
3. User answers each question
4. Answers are compared with ideal answers using NLP techniques
5. System calculates similarity score
6. Final score and feedback are displayed

---

## 📂 Project Structure

```id="p1z6a3"
ai-interview-bot/
│
├── app.py              # Main Streamlit app
├── utils.py            # Helper functions
├── requirements.txt    # Dependencies
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash id="j1h2k9"
git clone https://github.com/your-username/ai-interview-bot.git
cd ai-interview-bot
```

### 2. Install dependencies

```bash id="x8m4z2"
pip install -r requirements.txt
```

### 3. Run the application

```bash id="v9q7w1"
streamlit run app.py
```

---

## 📊 Output

* Displays generated interview questions
* Accepts user answers
* Shows individual scores
* Provides final evaluation score

---

## 🚀 Future Improvements

* Add LLM-based evaluation (HuggingFace / GPT)
* Resume upload feature
* Voice-based interview system
* Dashboard for performance tracking
* Database integration

---

## 📌 Conclusion

This project provides a basic implementation of an AI-driven interview system. It highlights how NLP techniques can be used to evaluate text responses and simulate real-world interview scenarios.

---

## 🙌 Author

**Jyothi Reddy**

[1]: https://discuss.streamlit.io/t/ai-interviewer-customized-interview-preparation-with-generative-ai/49011?utm_source=chatgpt.com "AI Interviewer: Customized interview preparation with generative AI - Show the Community! - Streamlit"
