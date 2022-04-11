from bs4 import BeautifulSoup
import requests

from modules.variables import HOME_PAGE_URL


def get_books_urls(category):
    """
    Permet de récupérer une liste des urls de tous les livres contenus dans une catégorie donnée,
    en gérant la pagination.

        Parameters:
            category (str): contient la seconde moitié de l'url d'une catégorie

        Returns:
            books_url (list): renvoie une liste d'urls (str) de livres
    """

    books_url = []
    base_category_url = HOME_PAGE_URL + category

    i = 1
    while True:
        category_url = base_category_url
        if i > 1:
            category_url = base_category_url.replace("index.html", f"page-{i}.html")
        page = requests.get(category_url)

        if page.status_code != 200:
            # on a atteint la dernière page
            break

        page = requests.get(category_url)
        soup = BeautifulSoup(page.content, "html.parser")
        all_books = soup.select("h3 > a")

        for book in all_books:
            base_book_url = str(book.get("href")).strip("../../..")
            book_url = HOME_PAGE_URL + "catalogue/" + base_book_url
            books_url.append(book_url)
        i += 1
    return books_url
