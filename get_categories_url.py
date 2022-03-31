from bs4 import BeautifulSoup
import requests


def get_categories_urls(home_page_url):

    home_page = requests.get(home_page_url)
    soup = BeautifulSoup(home_page.content, "html.parser")

    all_categories = soup.select("ul.nav-list > li > ul > li > a")

    categories_urls = []

    for category in all_categories:
        categories_urls.append(category.get("href"))

    return categories_urls


if __name__ == "__main__":
    print(get_categories_urls("http://books.toscrape.com/"))
