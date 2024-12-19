import requests
from bs4 import BeautifulSoup
from ner_extractor import extract_company

# Scrape and process the data
def scrapeData(max_articles=3):
    # URL to scrape
    url = "https://finance.yahoo.com/"

    # Send a GET request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the news articles
    articles = soup.find_all("div", class_="content")

    # Array to store the results
    articles_data = []

    # Loop through the articles with a counter
    for i, article in enumerate(articles):
        if i >= max_articles:
            break

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

        # Extract company names with the NER model
        company = extract_company(article_title, article_text)

        # Append the data as a dictionary to the list
        articles_data.append({
            "title": article_title,
            "text": article_text,
            "link": article_link,
            "company": company
        })

    return articles_data