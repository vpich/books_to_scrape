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

# def check_number_pages(url, page):
#     page_to_check_url = home_page_url + str(url).replace("index.html", page)
#     page_to_check = requests.get(page_to_check_url)
#     if page_to_check.status_code == 200:
#         return page_to_check_url
#     else:
#         return url




if __name__ == "__main__":
    #print(get_categories("http://books.toscrape.com/"))
    check_number_pages("https://books.toscrape.com/catalogue/category/books/mystery_3/index.html")
