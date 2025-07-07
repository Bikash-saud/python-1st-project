import requests  
from bs4 import BeautifulSoup  
import csv

url = "https://books.toscrape.com/"

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
        books.append([title, currency, price])

    # Save to CSV file
    with open("books.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Currency", "Price"]) 
        writer.writerows(books)

    print("Data has been written to books.csv")

scrape_books(url)