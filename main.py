from scraper import scrapeData
from sqlite import create_articles_table, drop_articles_table, get_all_articles
from export_to_csv import export_to_csv

# Get all articles and print
# all_articles = get_all_articles()
# print(all_articles)
# exit(0)

# Create SQLite database and table
drop_articles_table()
create_articles_table()

# Scrape data
articles = scrapeData()

# Export the articles to a CSV file
export_to_csv()