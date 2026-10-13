import csv
import os

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
OUTPUT_PATH = "output/books.csv"


def fetch_page(url):
    response = requests.get(url, timeout=10)
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


def save_to_csv(books, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price"])
        writer.writeheader()
        writer.writerows(books)


def main():
    html = fetch_page(URL)
    books = parse_books(html)
    save_to_csv(books, OUTPUT_PATH)
    print(f"Saved {len(books)} books to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
