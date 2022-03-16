from bs4 import BeautifulSoup
import requests

home_page_url = "http://books.toscrape.com/"
home_page = requests.get(home_page_url)
soup = BeautifulSoup(home_page.content, "html.parser")

all_categories = soup.select("ul.nav-list > li > ul > li > a")

categories_url = []

for cat in all_categories:
    categories_url.append(cat.get("href"))

if __name__ == "__main__":
    print(categories_url[1])
