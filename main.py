from scraper import scrape_and_return
from ner_extractor import extract_companies

# Get articles
articles = scrape_and_return()
print(articles)