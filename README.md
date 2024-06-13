# SpamShield: The SMS Sentry

SpamShield is a tool designed to classify SMS messages as either spam or not spam. It utilizes a machine learning model trained on processed text data to make predictions.

## Usage

1. **Enter the Message:**
   
    Input the SMS message you want to classify into the text area.

2. **Predict:**
   
    Click the "Predict" button to classify the SMS message as spam or not spam.

## Text Processing

The input text undergoes several preprocessing steps before being fed into the machine learning model:

1. **Lowercasing:**
   
    Convert the text to lowercase.

2. **Tokenization:**
   
    Split the text into individual words.

3. **Alphanumeric Filtering:**
   
    Remove any non-alphanumeric characters.

4. **Stopword and Punctuation Removal:**
   
    Exclude common stopwords (e.g., "the", "is") and punctuation marks.

5. **Stemming:**
   
    Reduce words to their root form using the Porter stemming algorithm.

## Model Prediction

1. **Vectorization:**
   
    Vectorize the preprocessed text using a TF-IDF vectorizer.

2. **Prediction:**
   
    Use a machine learning model to predict whether the message is spam or not spam.

3. **Display:**
   
    Display the prediction result as a header indicating whether the message is classified as spam or not.

## Dependencies

- Streamlit: `streamlit`
- NLTK: `nltk`
- Pickle: Standard library
- String: Standard library

## Models

- TF-IDF Vectorizer: `vectorizer.pkl`
- Machine Learning Model: `model.pkl`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features you'd like to see.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
