from bs4 import BeautifulSoup
import requests


def get_categories(url):

    home_page = requests.get(url)
    soup = BeautifulSoup(home_page.content, "html.parser")

    all_categories = soup.select("ul.nav-list > li > ul > li > a")

    categories_url = []

    for cat in all_categories:
        categories_url.append(cat.get("href"))

    return categories_url


if __name__ == "__main__":
    print(get_categories("http://books.toscrape.com/"))
