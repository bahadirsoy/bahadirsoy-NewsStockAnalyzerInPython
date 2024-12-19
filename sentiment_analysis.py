from transformers import pipeline

# Create a sentiment analysis pipeline
nlp_sentiment = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    sentiment = nlp_sentiment(text)
    return sentiment

text = "Apple is the best company"
sentiment_result = analyze_sentiment(text)
print(sentiment_result)