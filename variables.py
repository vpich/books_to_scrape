from bs4 import BeautifulSoup
import requests


def get_book_datas(product_page_url):
    page = requests.get(product_page_url)
    soup = BeautifulSoup(page.content, "html.parser")

    product_informations = soup.find_all("td")
    universal_product_code = [product_informations[0].string]
    price_including_tax = [product_informations[3].string]
    price_excluding_tax = [product_informations[2].string]
    available = product_informations[5].string
    number_available = [str(available).strip("Instock (avaible)")]

    title = [soup.find("h1").string]
    category = [soup.select("li > a")[2].string]
    product_description = [soup.select_one("article.product_page > p").string]
    review_rating = [soup.find("p", class_="star-rating").get("class")[1]]
    image_url = [soup.find("img").get("src")]

    datas = [
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

    return datas


if __name__ == "__main__":
    print(get_book_datas("https://books.toscrape.com/catalogue/avatar-the-last-airbender-smoke-and-shadow-part-3-smoke-and-shadow-3_881/index.html"))
