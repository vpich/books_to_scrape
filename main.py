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
    all_categories_list = []

    for book_url in all_books_url:
        book_data = get_book_datas(book_url)
        all_books_list.append(book_data)
        book_category = book_data[7]

        if book_category not in all_categories_list:
            all_categories_list.append(book_category)

    #     get_images(book_data[9], book_data[1], book_category)
    # save_data_to_csv("data.csv", all_books_list)


    # Le code ci-dessous devrait permettre de séparer chaque catégorie dans des fichiers csv disctincts, mais ne fonctionne pas

    # actuellement j'ai une liste de tous les livres, et chaque livre contient la liste de toutes ses data
    # je souhaite ranger les livres dans des liste pour chaque catégorie

    # je récupère la liste de toutes les catégorie
    # pour chaque livre
        # je compare si sa catégorie corresponds à l'indice i
        # si oui, je l'ajoute à la liste
    # je crée le fichier csv pour la catégorie
    # j'incrémente 1
    # je recommence la boucle pour faire la comparaison sur l'indice suivant

    i = 0
    while i < len(all_categories_list):
        books_in_cat = []
        for book_data in all_books_list:
            if book_data[7] == all_categories_list[i]:
                books_in_cat.append(book_data)
            save_data_to_csv(book_data[7], books_in_cat)
        i += 1







