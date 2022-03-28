import csv

from variables import get_book_datas
from get_categories_url import get_categories
from get_books_url import get_all_books

home_page_url = "http://books.toscrape.com/"


if __name__ == "__main__":

    categories_url_list = get_categories(home_page_url)
    all_books_url = []

    for category in categories_url_list:
        books_in_category = get_all_books_urls(category)
        for book in books_in_category:
            all_books_url.append(book)

    header_titles = [
        "product_page_url",
        "universal_product_code",
        "title",
        "price_including_tax",
        "price_excluding_tax",
        "number_available",
        "product_description",
        "category",
        "review_rating",
        "image_url"
    ]

    all_books_list = []

    for book_url in all_books_url:
        book_data = get_book_datas(book_url)
        all_books_list.append(book_data)

    with open("databis.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header_titles)
        for book in all_books_list:
            writer.writerow(book)
        # writer.writerow(all_books_dict)
        # writer.writerow(all_books_dict.values())

all_books_bis = [
    {"title": "xxx", "category": "xxx", "image_url": "xxx"},
    {"title": "xxx", "category": "xxx", "image_url": "xxx"},
]

# le faire sans images, et sans pagination d'abord
# problèmes avec les noms des fichiers
# problème avec la pagination