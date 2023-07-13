import pickle
import streamlit as st
from win32com.client import Dispatch


def speak(text):
   speak = Dispatch("SAPI.SpVoice")
   speak.Speak(text)


model1 = pickle.load(open("spam.pkl", "rb"))
cv = pickle.load(open("file.pkl", "rb"))


def main():
    st.title("Email Spam Classifier")
    # st.subheader("Build with Streamlit & Python")
    msg = st.text_area("Enter a Text: ")
    if st.button("Predict"):
        data = [msg]
        vect = cv.transform(data).toarray()
        prediction = model1.predict(vect)
        result = prediction[0]
        if result == 1:
            st.error("This is a spam mail")
            speak("This is a spam mail")
        else:
            st.success("This is a ham mail")


main()
