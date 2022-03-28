from bs4 import BeautifulSoup
import requests
from get_categories_url import get_categories

home_page_url = "http://books.toscrape.com/"


def check_number_pages(url):
    page_to_check = requests.get(url)
    soup = BeautifulSoup(page_to_check.content, "html.parser")

    next_button = soup.find_all("div", class_="next")
    print(next_button)

    if page_to_check.status_code == 200:
        pass


def get_all_books(category):

    books_url = []
    base_category_url = home_page_url + category

    for i in range(20):
    # i = 0
    # while True:

        category_url = base_category_url
        if i > 0:
            category_url = base_category_url.replace("index.html", "page-" + i + ".html")
        page = requests.get(category_url)
        if i == 1:
            pass
        if page.status_code != 200:
            break
        soup = BeautifulSoup(page.content, "html.parser")

        all_books = soup.select("h3 > a")

        for book in all_books:
            book_url = str(book.get("href")).strip("../../..")
            books_url.append(home_page_url + "catalogue/" + book_url)
        # i += 1
    return books_url


if __name__ == "__main__":
    print(get_all_books(get_categories(home_page_url)[0]))
