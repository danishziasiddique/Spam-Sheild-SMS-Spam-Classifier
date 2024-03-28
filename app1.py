import streamlit as st
import pickle
import nltk
import string

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
# Text Processing Function
def process_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    text2 = []
    for i in text:
        if i.isalnum():
            text2.append(i)
    text = text2[:]
    text2.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            text2.append(i)

    text = text2[:]
    text2.clear()

    for i in text:
        text2.append(ps.stem(i))

    return ' '.join(text2)


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
st.title('SpamShield')
st.caption('The SMS Sentry')


input_sms = st.text_area('Enter the message')

if st.button('Predict'):
    # 1)Preprocess
    Processed_sms = process_text(input_sms)
    # 2)Vectorize
    vector_input = tfidf.transform([Processed_sms])
    # 3)Predict
    prediction = model.predict(vector_input)[0]
    # 4)Display
    if prediction == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')




