from bs4 import BeautifulSoup
import requests
from get_categories_url import get_categories

home_page_url = "http://books.toscrape.com/"


def get_all_books_urls(category):

    books_url = []
    base_category_url = home_page_url + category

    i = 0
    while True:
        category_url = base_category_url
        if i > 1:
            category_url = base_category_url.replace("index.html", "page-" + str(i) + ".html")
        page = requests.get(category_url)
        if i == 1:
            pass
        if page.status_code != 200:
            break

        soup = BeautifulSoup(page.content, "html.parser")
        all_books = soup.select("h3 > a")

        for book in all_books:
            base_book_url = str(book.get("href")).strip("../../..")
            book_url = home_page_url + "catalogue/" + base_book_url
            if book_url in books_url:
                break
            books_url.append(book_url)
        i += 1
    return books_url


if __name__ == "__main__":
    print(get_all_books_urls(get_categories(home_page_url)[0]))
