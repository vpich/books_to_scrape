import csv

from variables import get_book_datas
from get_categories_url import get_categories
from get_books_url import get_all_books

home_page_url = "http://books.toscrape.com/"


if __name__ == "__main__":

    all_books_list = []
    categories_url_list = get_categories(home_page_url)

    for category in categories_url_list:
        books_in_category = get_all_books(category)
        for book in books_in_category:
            all_books_list.append(book)

    for book in all_books_list:
        all_books_datas = get_book_datas(book)

    # all_books_dict = {}
    #
    # with open("data.csv", "w", encoding="utf-8") as f:
    #     writer = csv.writer(f, delimiter=",")
    #     writer.writerow(all_books_dict)
    #     writer.writerow(all_books_dict.values())
    # toutes ces infos dans un excel

# le faire sans images, et sans pagination d'abord
# problèmes avec les noms des fichiers
# problème avec la pagination