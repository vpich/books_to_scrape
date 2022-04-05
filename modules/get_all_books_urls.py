from modules.get_categories_urls import get_categories_urls
from modules.get_books_urls import get_all_books_urls
from modules.variables import HOME_PAGE_URL


def get_all_urls_in_dict():

    all_categories_urls = get_categories_urls(HOME_PAGE_URL)
    all_books_urls = {}

    for category_url in all_categories_urls:
        books_urls_in_category = get_all_books_urls(category_url)
        category = category_url.split("/")[3]
        all_books_urls[category] = books_urls_in_category

    return all_books_urls


if __name__ == "__main__":
    print(get_all_urls_in_dict())
