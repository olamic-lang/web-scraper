import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"


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


def main():
    html = fetch_page(URL)
    books = parse_books(html)
    for book in books[:5]:
        print(book["title"], "-", book["price"])
    print(f"Found {len(books)} books")


if __name__ == "__main__":
    main()
