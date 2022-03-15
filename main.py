from bs4 import BeautifulSoup
import requests

product_page_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(product_page_url)
soup = BeautifulSoup(page.content, "html.parser")

# Element à scrapper:
# product_page_url              =>
# universal_product_code (upc)  =>
# title                         =>
# price_including_tax           =>
# price_excluding_tax           =>
# number_available              =>
# product_description           =>
# category                      =>
# review_rating                 =>
# image_url                     =>

