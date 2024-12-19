from scraper import scrape_and_return

# Get articles
articles = scrape_and_return()

# Print the articles
for article in articles:
    print("Title:", article["title"])
    print("Text:", article["text"])
    print("Link:", article["link"])
    print("-" * 50)