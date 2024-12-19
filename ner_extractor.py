from transformers import pipeline

# Initialize NER pipeline
ner_model = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

def extract_companies(article_text):
    ner_results = ner_model(article_text)
    print("NER Results:", ner_results)

    # Extract company names
    companies = [
        entity["word"]
        for entity in ner_results
        if "ORG" in entity["entity"]
    ]
    return companies