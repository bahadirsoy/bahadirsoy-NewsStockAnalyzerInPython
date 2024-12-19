import sqlite3

# Create SQLite database and table
def create_database():
    conn = sqlite3.connect("news_stock_analyzer.db")
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        text TEXT,
                        link TEXT,
                        company TEXT,
                        sentiment TEXT)''')

    conn.commit()
    conn.close()


# Store the scraped and analyzed data
def store_in_database(articles_data):
    conn = sqlite3.connect("news_stock_analyzer.db")
    cursor = conn.cursor()

    # Insert data into the articles table
    for article in articles_data:
        cursor.execute('''INSERT INTO articles (title, text, link, company, sentiment)
                          VALUES (?, ?, ?, ?, ?)''',
                       (article["title"], article["text"], article["link"], article["company"], article["sentiment"]))

    conn.commit()
    conn.close()