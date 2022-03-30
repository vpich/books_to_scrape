from get_images import get_images
from save_data_to_csv import save_data_to_csv
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

    all_books_list = []

    for book_url in all_books_url:
        book_data = get_book_datas(book_url)
        all_books_list.append(book_data)
        book_category = book_data[7]

        get_images(book_data[9], book_data[1], book_category)

    save_data_to_csv("data.csv", all_books_list)

    # Le code ci-dessous devrait permettre de séparer chaque catégorie dans des fichiers csv disctincts, mais ne fonctionne pas
    books_per_cat = {}
    for book in all_books_list:
        books_per_cat[book[7]].append(book)

    for category in books_per_cat:
        save_data_to_csv(category, books_per_cat[category])
