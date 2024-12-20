from transformers import pipeline

# Create a sentiment analysis pipeline
nlp_sentiment = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    # Truncate text to fit within the model's max length (512 tokens)
    max_length = 512
    text = text[:max_length]

    sentiment = nlp_sentiment(text)
    return sentiment[0]["label"]