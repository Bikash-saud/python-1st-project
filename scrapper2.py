# scrapper-py > ...
# go to git bash

# git config • global user name "

# same with gmail
# homeworkpy
# 
# git init git
# status => if you want to check what thestatus of files is
# git add.
# git commit -m "your message here"
# copy paste git code from git hub
# git push =› to send
from bs4 import Beautifulsoup

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
        writer.writerow(["Title", "Currency", "Price"])  # Header row
        writer.writerows(books)

    print("Data has been written to books.csv")

scrape_books(url)