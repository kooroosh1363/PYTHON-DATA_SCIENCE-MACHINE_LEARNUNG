import streamlit as st
import pandas as pd
import emoji
import requests  # برای درخواست اطلاعات از URL
from bs4 import BeautifulSoup

import numpy as np
import os
import joblib

# Import توابع مربوط به NLTK
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

import nltk

nltk.download("punkt")

# create object from SnowballStemmer
stemmer = SnowballStemmer("english")

st.markdown(
    """
    <style>
    
    .st-af {
        background-color: hsla(219, 44%, 51%, 0.59); 
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache(allow_output_mutation=True)
def load_ml_model():
    label_encoder_model = joblib.load("./label.h5")
    vectorizer = joblib.load("./model_1.h5")
    svmc = joblib.load("./model_2.h5")

    with open("./stopwords.txt", "r", encoding="utf-8") as f:
        stopwords = f.read().splitlines()

    return label_encoder_model, vectorizer, svmc, stopwords


# تابع تشخیص مشخصه‌های متن
def predict_category(text, label_encoder_model, vectorizer, svmc, stopwords):
    # پردازش متن ورودی
    title_body_tokenized = word_tokenize(text)
    title_body_tokenized_filtered = [
        w for w in title_body_tokenized if w not in stopwords
    ]
    title_body_tokenized_filtered_stemmed = [
        stemmer.stem(w) for w in title_body_tokenized_filtered
    ]
    preprocessed_text = " ".join(title_body_tokenized_filtered_stemmed)

    # TF-IDF  تبدیل متن به بردار عددی
    text_vector = vectorizer.transform([preprocessed_text])

    # پیش‌بینی مشخصه با استفاده از مدل SVM
    category_encoded = svmc.predict(text_vector)

    # ترجمه مشخصه به مقدار اصلی
    category = label_encoder_model.inverse_transform(category_encoded)

    return category[0]


@st.cache(allow_output_mutation=True)
def analyze_category(text, label_encoder_model, vectorizer, svmc, stopwords):
    result = predict_category(text, label_encoder_model, vectorizer, svmc, stopwords)
    return result


def main():
    st.title("News or text category analysis")

    activities = ["Text Characteristics", "URL Analysis", "About"]
    choice = st.sidebar.selectbox("Pages", activities)

    label_encoder_model, vectorizer, svmc, stopwords = load_ml_model()

    if choice == "Text Characteristics":
        st.write(emoji.emojize("Please Enter Your Text Or News :writing_hand:"))
        raw_text = st.text_area("Please enter your English or Farsi text or news", "Example ")
        if st.button("analysis"):
            result = analyze_category(
                raw_text, label_encoder_model, vectorizer, svmc, stopwords
            )
            st.success("Category of news or text:{}".format(result))

    if choice == "URL Analysis":
        st.write(emoji.emojize("Please Enter URL of the website :globe_with_meridians:"))
        url = st.text_input("Enter the URL of the website", "")
        if st.button("Analyze URL"):
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text()
                result = analyze_category(
                    text, label_encoder_model, vectorizer, svmc, stopwords
                )
                st.success("Category of the website content:{}".format(result))
            except Exception as e:
                st.error("An error occurred: {}".format(e))

    if choice == "About":
        st.subheader("Exercise 14: This web page was created using Streamlit, which allows the user to enter English or Farsi texts and then see their category analysis.")
        st.info("peyman  radmanesh ")
        st.text("https://filoger.com/")


if __name__ == "__main__":
    main()
