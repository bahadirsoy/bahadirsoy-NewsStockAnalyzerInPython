from transformers import BertTokenizer, BertForTokenClassification
from transformers import pipeline

# Load the model
model_name = "dslim/bert-base-NER"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name)

# Create a NER pipeline
nlp_ner = pipeline("ner", model=model, tokenizer=tokenizer)


def extract_single_company_from_ner(title, ner_results):
    # Check if the title mentioned a company
    title_companies = [entity["word"] for entity in ner_results if "ORG" in entity["entity"]]

    # If companies are found in the title, return the first one
    if title_companies:
        for company in title_companies:
            if company.lower() in title.lower():
                return company

    # If no company in title, select the company with the highest confidence value
    companies_with_scores = [
        (entity["word"], entity["score"])
        for entity in ner_results
        if "ORG" in entity["entity"]
    ]

    if companies_with_scores:
        # Sort by score and return the company with the highest confidence
        companies_with_scores.sort(key=lambda x: x[1], reverse=True)
        return companies_with_scores[0][0]

    return None


def extract_company(title, text):
    ner_results = nlp_ner(text)
    print(ner_results)

    company = extract_single_company_from_ner(title, ner_results)

    return company