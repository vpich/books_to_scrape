import csv

from get_images import get_images
from variables import get_book_datas
from get_categories_url import get_categories
from get_books_url import get_all_books_urls

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

        get_images(book_data[9], book_data[1])

    with open("data.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header_titles)
        for book in all_books_list:
            writer.writerow(book)



# oubli: chaque categorie doit être un fichier dans un fichier csv différent