from scraper import scrapeData
from sqlite import create_database

# Create SQLite database and table
create_database()

# Get articles
articles = scrapeData()
print(articles)