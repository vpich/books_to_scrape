[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# books_to_scrape

## About The Project
books_to_scrape permet de récupérer des informations sur les livres du site exemple https://books.toscrape.com/ et des les enregistrer dans un fichier csv pour chaque catégorie de livres.
Il permet également de télécharger toutes les images de ces livres dans un dossier, trié par catégorie.

## Technologies
- Python 3.10

## Getting Started

### Installation (Windows)
1. Pour installer Python, vous pouvez vous rendre sur https://wiki.python.org/moin/BeginnersGuide/Download
2. Pour créer un environnement virtuel, saisissez dans votre terminal à l'endroit où vous souhaitez le créer:
   - `python -m venv env`
3. Pour activer votre environnement, saisissez:
   - `source env/Scripts/activate`
4. Votre environnement est activé et vous devriez voir apparaitre `(env)` à chaque début de ligne
5. Il vous faudra ensuite installer les packages dans votre environnement avec la commande ci-dessous
   - `pip install -r requirements.txt`

### Usage
- Pour exécuter le web scraping, utilisez dans votre terminal la commande suivante:
  - `python main.py`

## Features
- Gestion de la pagination
- Renommage des images téléchargées avec leur propre code UPC (universal product code)
- Création des dossiers et sous-dossiers images et csv même s'ils n'existent pas

## Author
Vpich
