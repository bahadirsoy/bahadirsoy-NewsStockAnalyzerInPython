import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://finance.yahoo.com/"

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all the news articles
articles = soup.find_all("div", class_="content")

# Loop through the articles
for article in articles:
    article_a_tag = article.find("a")
    article_title = article_a_tag["title"]
    article_link = article_a_tag["href"]

    # GET request to the article link
    article_response = requests.get(article_link)
    article_soup = BeautifulSoup(article_response.content, "html.parser")

    # Find the article content
    article_content = article_soup.find("div", class_="body")

    # Get all p elements and concat the strings
    p_elements = article_content.find_all("p")
    article_text = " ".join([p.text for p in p_elements])

    # Print the article title and text
    print("Title:", article_title)
    print("Text:", article_text)
    print("Link:", article_link)
    print("-" * 50)
    print()