from bs4 import BeautifulSoup
import requests

from modules.variables import HOME_PAGE_URL


def get_categories_urls():
    """ Permets de récupérer une liste avec la seconde moitié des urls de toutes les catégories """
    home_page = requests.get(HOME_PAGE_URL)
    soup = BeautifulSoup(home_page.content, "html.parser")

    all_categories = soup.select("ul.nav-list > li > ul > li > a")

    categories_urls = []

    for category in all_categories:
        categories_urls.append(category.get("href"))

    return categories_urls


if __name__ == "__main__":
    print(get_categories_urls())
