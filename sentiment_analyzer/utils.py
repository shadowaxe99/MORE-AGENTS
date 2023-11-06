```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import pipeline

nltk.download('vader_lexicon')

def process_text(text):
    """
    Function to preprocess text for sentiment analysis.
    """
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    
    # Remove punctuation
    tokens = [word for word in tokens if word.isalnum()]
    
    return ' '.join(tokens)

def analyze_sentiment_vader(text):
    """
    Function to analyze sentiment using NLTK's Vader.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    
    return sentiment

def analyze_sentiment_transformers(text):
    """
    Function to analyze sentiment using Hugging Face Transformers.
    """
    sentiment_analysis = pipeline("sentiment-analysis")
    result = sentiment_analysis(text)[0]
    
    return result
```