# News Stock Analyzer

## Overview
The News Stock Analyzer is a Python project that scrapes financial news articles, identifies company names using a pre-trained Named Entity Recognition (NER) model, analyzes the sentiment of the articles, and stores the results in an SQLite database. The data can then be exported to a CSV file for further analysis.

## Features
Scrapes news articles from [Yahoo Finance](https://finance.yahoo.com/).
Extracts company names using a pre-trained NER model.
Analyzes sentiment of the articles using a pre-trained model.
Stores results in an SQLite database.
Exports the stored data to a CSV file.

## Requirements
- Python 3.10
- Required libraries
  - `beautifulsoup4`
  - `requests`
  - `python-dotenv`
  - `transformers`
  - `sqlite3`

## Installation

**Clone the Repository:**
   ```bash
   git clone https://github.com/bahadirsoy/bahadirsoy-NewsStockAnalyzerInPython.git
   ```

**Set Up Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   DATABASE_NAME=news_stock_analyzer.db
   MAX_ARTICLES=5
   DEBUG=true
   ```

**Install Dependencies:**
   Install the required Python libraries

## Usage

### 1. Run the Main Script
The main script scrapes data, analyzes it, and stores it in the SQLite database. Then, it exports the data to a CSV file.:
```bash
python main.py
```
