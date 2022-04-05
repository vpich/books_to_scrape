import csv
from pathlib import Path

HEADER_TITLES = [
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


def save_data_to_csv(csv_name, books_list):

    csv_directory = Path("csv")
    if not csv_directory.exists():
        csv_directory.mkdir()

    with open(f"{csv_directory}/{csv_name}.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(HEADER_TITLES)
        for book in books_list:
            writer.writerow(book)
