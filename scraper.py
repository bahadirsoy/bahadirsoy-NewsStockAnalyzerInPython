import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from ner_extractor import extract_company
from sentiment_analysis import analyze_sentiment
from sqlite import store_in_database

load_dotenv()

# Scrape and process the data
def scrapeData(max_articles=int(os.getenv("MAX_ARTICLES"))):
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
        if article_content is None:
            # Check for the second scenario with 'data-article-body="true"'
            article_content = article_soup.find("div", {"data-article-body": "true"})

        if article_content is None:
            if os.getenv("DEBUG") == "true": print("No content found for article:", article_title)
            continue

        # Get all p elements and concat the strings
        p_elements = article_content.find_all("p")
        article_text = " ".join([p.text for p in p_elements])

        # Extract company names with the NER model
        company = extract_company(article_title, article_text)

        # Analyze the sentiment of the article
        sentiment = analyze_sentiment(article_text)

        # Extract the publication date
        time_tag = article_soup.find("time", class_="byline-attr-meta-time")
        if time_tag and "datetime" in time_tag.attrs:
            article_date = time_tag["datetime"].split("T")[0]  # Extract only the date part (YYYY-MM-DD)
        else:
            article_date = None

        # Append the data as a dictionary to the list
        articles_data.append({
            "title": article_title,
            "text": article_text,
            "link": article_link,
            "company": company,
            "sentiment": sentiment,
            "date": article_date
        })

        # Print the article
        if os.getenv("DEBUG") == "true":
            print(f"Article {i + 1}: {article_title}"
                  f"\nText: {article_text}"
                  f"\nLink: {article_link}"
                  f"\nCompany: {company}"
                  f"\nSentiment: {sentiment}"
                  f"\nDate: {article_date}\n")
            print("-" * 50)

        # Insert the data into the database
        store_in_database(articles_data)

    return articles_data