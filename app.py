import streamlit as st
import pickle
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def load_tfidf():
    tfidf = pickle.load(open("tf_idf.pkt", "rb"))
    return tfidf

def load_model():
    nb_model = pickle.load(open("toxicity_model.pkt", "rb"))
    return nb_model

def toxicity_detection(text):
    tfidf = load_tfidf()
    text_tfidf = tfidf.transform([text]).toarray()
    model = load_model()  # Call the function to get the model instance
    prediction = model.predict(text_tfidf)
    
    class_name = "Toxic" if prediction == 1 else "Non-Toxic"

    return class_name

st.header("Toxicity Detection App")
st.subheader("Enter the text below")
text_input = st.text_input("Enter your text")

if text_input is not None:
    if st.button('Analyze'):
        result = toxicity_detection(text_input)
        st.subheader('Detected result is below')
        st.info('The result is ' + result + '.')
