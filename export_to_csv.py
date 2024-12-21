import csv
import os
from dotenv import load_dotenv
from sqlite import get_all_articles

def export_to_csv(output_file="exported_articles.csv"):
    # Fetch all articles from the database
    articles = get_all_articles()

    # Define the header
    header = ["ids", "title", "text", "company", "sentiment", "date"]

    # Write data to a CSV file
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")

        # Write the header
        writer.writerow(header)

        # Write the rows
        for article in articles:
            writer.writerow(article)

    if os.getenv("DEBUG") == "true": print(f"Data exported successfully to {output_file}")