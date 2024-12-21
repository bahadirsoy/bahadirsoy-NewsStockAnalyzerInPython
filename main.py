from scraper import scrapeData
from sqlite import create_articles_table, drop_articles_table
from export_to_csv import export_to_csv

# Create SQLite database and table
drop_articles_table()
create_articles_table()

# Scrape data
articles = scrapeData()

# Export the articles to a CSV file
export_to_csv()