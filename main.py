from scraper import scrape_and_return
from ner_extractor import extract_companies

# Get articles
# articles = scrape_and_return()
# print(articles)

example_text = "Apple Inc. reported a rise in quarterly revenue, while Microsoft and Google saw a decline."

# Extract companies
companies = extract_companies(example_text)
print("Extracted Companies:", companies)