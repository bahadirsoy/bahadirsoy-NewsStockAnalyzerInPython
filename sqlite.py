import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

# Create SQLite database and table
def create_articles_table():
    conn = sqlite3.connect(os.getenv("DATABASE_NAME"))
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        text TEXT,
                        company TEXT,
                        sentiment TEXT,
                        date TEXT)''')

    conn.commit()
    conn.close()


# Store the scraped and analyzed data
def store_in_database(articles_data):
    conn = sqlite3.connect(os.getenv("DATABASE_NAME"))
    cursor = conn.cursor()

    # Insert data into the articles table
    for article in articles_data:
        cursor.execute('''INSERT INTO articles (title, text, company, sentiment, date)
                                  VALUES (?, ?, ?, ?, ?)''',
                       (article["title"], article["text"], article["company"], article["sentiment"], article["date"]))

    conn.commit()
    conn.close()


def get_all_articles():
    conn = sqlite3.connect(os.getenv("DATABASE_NAME"))
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM articles")
    rows = cursor.fetchall()

    conn.close()
    return rows

def drop_articles_table():
    conn = sqlite3.connect(os.getenv("DATABASE_NAME"))
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS articles")

    conn.commit()
    conn.close()

allArticles = get_all_articles()
print(allArticles)