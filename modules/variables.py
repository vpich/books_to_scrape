from bs4 import BeautifulSoup
import requests

HOME_PAGE_URL = "http://books.toscrape.com/"


def get_book_data(product_page_url):
    """ Parse la page d'un produit et renvoie une liste contenant les données pour l'étude de marché """
    page = requests.get(product_page_url)
    soup = BeautifulSoup(page.content, "html.parser")

    product_informations = soup.find_all("td")
    universal_product_code = product_informations[0].string
    price_including_tax = product_informations[3].string
    price_excluding_tax = product_informations[2].string
    available = product_informations[5].string
    number_available = str(available).strip("Instock (avaible)")

    title = soup.find("h1").string
    category = soup.select("li > a")[2].string
    product_description = soup.select_one("article.product_page > p")
    review_rating = soup.find("p", class_="star-rating").get("class")[1]
    image_url = HOME_PAGE_URL + str(soup.find("img").get("src")).replace("../../", "")

    # Certaines description peuvent être vide, cette condition permet d'éviter le renvoie d'une erreur
    if product_description is not None:
        product_description = soup.select_one("article.product_page > p").string
    else:
        product_description = ""

    data = [
        product_page_url,
        universal_product_code,
        title,
        price_including_tax,
        price_excluding_tax,
        number_available,
        product_description,
        category,
        review_rating,
        image_url
    ]

    return data
