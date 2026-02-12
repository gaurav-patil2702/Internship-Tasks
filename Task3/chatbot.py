
"""
Internship Task-3: AI Chatbot with NLP
Uses NLTK for basic NLP preprocessing and rule-based response generation.
"""

import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download('punkt')

# Knowledge Base
knowledge_base = [
    "Hello",
    "Hi",
    "What is your name?",
    "How are you?",
    "What is artificial intelligence?",
    "What is machine learning?",
    "What is NLP?",
    "Tell me about Python.",
    "What is data science?",
    "Bye"
]


responses = {
    "Hello": "Hello! How can I help you?",
    "Hi": "Hi there! What can I do for you?",
    "What is your name?": "I am an NLP-based AI chatbot.",
    "How are you?": "I am functioning properly!",
    "What is artificial intelligence?": "Artificial Intelligence is the simulation of human intelligence in machines.",
    "What is machine learning?": "Machine Learning is a subset of AI that allows systems to learn from data.",
    "What is NLP?": "NLP stands for Natural Language Processing. It helps computers understand human language.",
    "Tell me about Python.": "Python is a popular programming language used in AI, data science, and web development.",
    "What is data science?": "Data Science involves extracting insights from data using statistics and machine learning.",
    "Bye": "Goodbye! Have a great day!"
}

def preprocess(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    return " ".join(text)

def get_response(user_input):
    processed_input = preprocess(user_input)

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(knowledge_base + [processed_input])

    similarity = cosine_similarity(tfidf[-1], tfidf[:-1])
    index = similarity.argmax()

    if similarity[0][index] > 0.3:
        return responses[knowledge_base[index]]
    else:
        return "Sorry, I don't understand that question."

def chatbot():
    print("AI Chatbot (type 'bye' to exit)")
    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Bot:", responses["Bye"])
            break

        print("Bot:", get_response(user_input))

if __name__ == "__main__":
    chatbot()
