import requests
from pathlib import Path


def get_images(image_url, upc):
    image = requests.get(image_url).content
    image_type = Path(image_url).suffix
    with open(f'images/{upc}{image_type}', "wb") as f:
        f.write(image)


if __name__ == "__main__":
    get_images("https://books.toscrape.com/media/cache/9f/25/9f25ffe4229a32d1368b3dfe248c3343.jpg", "a897fe39b1053632")
