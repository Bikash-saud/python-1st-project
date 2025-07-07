import requests  
from bs4 import BeautifulSoup  
import json

url = "https://www.daraz.com.np/"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Cannot fetch data")
        return

    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")  
    articles = soup.find_all("article", class_="product_pod")

    books = []
    for article in articles:
        title = article.h3.a['title']
        price_text = article.find("p", class_="price_color").text
        currency = price_text[0]
        price = float(price_text[1:])
        books.append({
            "title": title,
            "currency": currency,
            "price": price
        })

    # Save to JSON file
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

    print("Data has been written to books.json")

scrape_books(url)