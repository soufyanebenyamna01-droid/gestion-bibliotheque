from bibliotheque.livre import Livre
from bibliotheque.catalogue import Catalogue
from bibliotheque.catalogue import Bibliotheque as Catalogue


def main():
    catalogue = Catalogue()
    # exemple : adapte selon tes classes
    # livre = Livre("Titre", "Auteur")
    # catalogue.ajouter(livre)
    print("Bibliothèque prête.")


if __name__ == "__main__":
    main()