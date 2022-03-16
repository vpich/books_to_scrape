from bs4 import BeautifulSoup
import requests
from get_categories_url import home_page_url, categories_url

current_category_url = home_page_url + categories_url[0]

current_cat = requests.get(current_category_url)
soup = BeautifulSoup(current_cat.content, "html.parser")

all_books = soup.select("h3 > a")

books_url = []

for book in all_books:
    book_url = str(book.get("href")).strip("../../..")
    books_url.append(home_page_url + "catalogue/" + book_url)

if __name__ == "__main__":
    print(current_category_url)
    print(books_url)
