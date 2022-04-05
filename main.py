from modules.save_images import save_images
from modules.save_data_to_csv import save_data_to_csv
from modules.variables import get_book_data
from modules.get_all_books_urls import get_all_urls_in_dict

ALL_BOOKS_URLS = get_all_urls_in_dict()


def save_all_images_and_csv(all_books_urls_dict):

    for category, books_of_category in all_books_urls_dict.items():
        all_books_list = []
        # def save_all_images_category
        for book_url in books_of_category:
            book_data = get_book_data(book_url)
            all_books_list.append(book_data)

            book_image_url = book_data[9]
            book_upc = book_data[1]

            save_images(book_image_url, book_upc, category)

        save_data_to_csv(category, all_books_list)


if __name__ == "__main__":
    save_all_images_and_csv(ALL_BOOKS_URLS)
