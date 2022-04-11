import requests
from pathlib import Path


def save_images(image_url, upc, directory_name):
    image = requests.get(image_url).content
    image_type = Path(image_url).suffix
    image_directory = Path(f"images/{directory_name}")

    if not image_directory.exists():
        image_directory.mkdir(parents=True)

    with open(f'{image_directory}/{upc}{image_type}', "wb") as f:
        f.write(image)
