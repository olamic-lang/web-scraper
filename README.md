# Books Web Scraper

A command-line web scraper built with Python that collects the title and price of every book from [Books to Scrape](https://books.toscrape.com/), a sandbox site made for practicing web scraping, and saves the results to a CSV file.

## Features

- Scrapes all 50 pages automatically, stopping when the site runs out of pages
- Extracts the full title and price of each book
- Saves results to `output/books.csv`
- Waits one second between requests to avoid overloading the server

## Requirements

- Python 3.9 or newer
- `requests` and `beautifulsoup4` (listed in `requirements.txt`)

## Setup

```bash
git clone https://github.com/olamic-lang/web-scraper.git
cd web-scraper
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python scraper.py
```

The scraper prints its progress page by page, then writes 1000 books to `output/books.csv`.

## Project Structure

```
web-scraper/
├── scraper.py          # fetching, parsing, pagination, and CSV output
├── requirements.txt    # pinned dependencies
├── README.md
└── .gitignore
```

## How It Works

1. `fetch_page` downloads a page and returns `None` on a 404, which signals the end of the catalogue.
2. `parse_books` uses BeautifulSoup and CSS selectors to extract each book's title and price.
3. `scrape_all_pages` loops through the pages, pausing between requests.
4. `save_to_csv` writes the collected data to disk.

## Responsible Scraping

This project targets a site built for practice. Before scraping a real website, check its `robots.txt` and terms of service, keep your request rate low, and never collect personal data.
