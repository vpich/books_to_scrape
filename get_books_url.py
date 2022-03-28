from bs4 import BeautifulSoup
import requests
from get_categories_url import get_categories

home_page_url = "http://books.toscrape.com/"


def get_all_books(category):

    category_url = home_page_url + category

    page = requests.get(category_url)
    soup = BeautifulSoup(page.content, "html.parser")

    all_books = soup.select("h3 > a")

    books_url = []

    for book in all_books:
        book_url = str(book.get("href")).strip("../../..")
        books_url.append(home_page_url + "catalogue/" + book_url)
    return books_url


if __name__ == "__main__":
    print(get_all_books(get_categories(home_page_url)[0]))
