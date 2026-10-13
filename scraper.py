import csv
import os
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
OUTPUT_PATH = "output/books.csv"
DELAY_SECONDS = 1


def fetch_page(url):
    response = requests.get(url, timeout=10)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    response.encoding = "utf-8"
    return response.text


def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    books = []
    for article in soup.select("article.product_pod"):
        title = article.h3.a["title"]
        price = article.select_one("p.price_color").text
        books.append({"title": title, "price": price})
    return books


def scrape_all_pages():
    books = []
    page = 1
    while True:
        html = fetch_page(BASE_URL.format(page))
        if html is None:
            break
        page_books = parse_books(html)
        books.extend(page_books)
        print(f"Page {page}: {len(page_books)} books")
        page += 1
        time.sleep(DELAY_SECONDS)
    return books


def save_to_csv(books, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price"])
        writer.writeheader()
        writer.writerows(books)


def main():
    books = scrape_all_pages()
    save_to_csv(books, OUTPUT_PATH)
    print(f"Saved {len(books)} books to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
