from get_images import save_images
from save_data_to_csv import save_data_to_csv
from variables import get_book_data
from get_categories_url import get_categories_urls
from get_books_url import get_all_books_urls

HOME_PAGE_URL = "http://books.toscrape.com/"

if __name__ == "__main__":

    all_categories_urls = get_categories_urls(HOME_PAGE_URL)
    all_books_urls = []

    for category_url in all_categories_urls:
        books_urls_in_category = get_all_books_urls(category_url)
        for book_url_in_category in books_urls_in_category:
            all_books_urls.append(book_url_in_category)

    all_books_list = []
    all_categories_list = []

    for book_url in all_books_urls:
        book_data = get_book_data(book_url)
        all_books_list.append(book_data)

        book_category = book_data[7]
        book_image_url = book_data[9]
        book_upc = book_data[1]

        if book_category not in all_categories_list:
            all_categories_list.append(book_category)

        save_images(book_image_url, book_upc, book_category)

    i = 0
    while i < len(all_categories_list):
        books_in_category = []
        for book_data in all_books_list:
            book_category = book_data[7]
            if book_category == all_categories_list[i]:
                books_in_category.append(book_data)
                save_data_to_csv(book_category, books_in_category)
        i += 1
