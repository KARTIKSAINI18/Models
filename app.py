import streamlit as st
import joblib

vectorizer = joblib.load('vectorizer.jb')
model = joblib.load('dt_model.jb')

st.title('Fake News Detector')
st.write('Enter a News Article below to check it is fake or Real')

news_input = st.text_area('News article:',"")

if st.button('Check News'):
    if news_input.strip():
        transform_input = vectorizer.transform([news_input])
        prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.success("The News is Real")
        else:
            st.error("The News is Fake")

    else:
        st.warning("Please enter some text to analyze.")