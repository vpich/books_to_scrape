from bs4 import BeautifulSoup
import requests

product_page_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(product_page_url)
soup = BeautifulSoup(page.content, "html.parser")

header_titles = [
    "product_page_url",
    "universal_product_code",
    "title",
    "price_including_tax",
    "price_excluding_tax",
    "number_available"
    "product_description"
    "category"
    "review_rating"
    "image_url"
]

product_informations = soup.find_all("td")
universal_product_code = product_informations[0].string
price_including_tax = product_informations[3].string
price_excluding_tax = product_informations[2].string
available = product_informations[5].string
number_available = str(available).strip("Instock (avaible)")


title = soup.find("h1").string
category = soup.select("li > a")[2].string
rating = soup.find("p", class_="star-rating")
product_description = soup.select_one("article.product_page > p").string
review_rating = soup.find("p", class_="star-rating").get("class")[1]
image_url = soup.find("img").get("src")

print(universal_product_code, price_including_tax, price_excluding_tax, available)
print(title)
print(product_description)
print(category)
print(image_url)
print(review_rating)
print(number_available)

with open("data.csv", "w") as f:
    pass

print(header_titles)