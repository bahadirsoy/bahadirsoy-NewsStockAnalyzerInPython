from scraper import scrapeData
from sqlite import create_articles_table
from sqlite import drop_articles_table

# Create SQLite database and table
drop_articles_table()
create_articles_table()

# Get articles
articles = scrapeData()
print(articles)