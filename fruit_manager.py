import json
import os

DATA_DIR = "data"
PRIX_PATH = os.path.join(DATA_DIR, "prix.json")
INVENTAIRE_PATH = os.path.join(DATA_DIR, "inventaire.json")
TRESORERIE_PATH = os.path.join(DATA_DIR, "tresorerie.txt")


def ouvrir_inventaire(path=INVENTAIRE_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        inventaire_defaut = {
            "bananes": 120,
            "mangues": 85,
            "ananas": 45,
            "noix de coco": 60,
            "papayes": 30,
        }
        with open(path, "w", encoding="utf-8") as fichier:
            json.dump(inventaire_defaut, fichier, ensure_ascii=False, indent=4)

    with open(path, "r", encoding="utf-8") as fichier:
        inventaire = json.load(fichier)
    return inventaire


def ecrire_inventaire(inventaire, path="data/inventaire.json"):
    with open(path, "w", encoding="utf-8") as fichier:

        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)


def ouvrir_tresorerie(path=TRESORERIE_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as fichier:
            json.dump(1000.0, fichier)

    with open(path, "r", encoding="utf-8") as fichier:
        tresorerie = json.load(fichier)
    return tresorerie


def ecrire_tresorerie(tresorerie, path="tresorerie.txt"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(tresorerie, fichier, ensure_ascii=False, indent=4)


def ouvrir_prix(path=PRIX_PATH):
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(path):
        prix_defaut = {
            "bananes": 2,
            "mangues": 7,
            "ananas": 5,
            "noix de coco": 4,
            "papayes": 3,
        }
        with open(path, "w", encoding="utf-8") as fichier:
            json.dump(prix_defaut, fichier, ensure_ascii=False, indent=4)

    with open(path, "r", encoding="utf-8") as fichier:
        prix = json.load(fichier)
    return prix


def afficher_tresorerie(tresorerie):
    print(f"la tresorerie actuelle est de {tresorerie} euros")


def afficher_inventaire(inventaire):
    print("l'inventaire actuel contient")
    for fruit, quantité in inventaire.items():
        print(f"{fruit.capitalize()} : {quantité} unités")


def recolter(inventaire, fruit, quantité):
    nouvelle_quantité = inventaire.get(fruit, 0) + quantité
    inventaire[fruit] = nouvelle_quantité
    ecrire_inventaire(inventaire)
    print(f"nous avons recolté {quantité} {fruit} supplémentaire")


def vendre_fruits(inventaire, fruit, quantité, tresorerie, prix):
    if inventaire.get(fruit, 0) >= quantité:
        inventaire[fruit] -= quantité
        ecrire_inventaire(inventaire)
        tresorerie += prix.get(fruit, 0) * quantité
        print(f"Vendu: {quantité} unités de {fruit}")
        return (inventaire, tresorerie)
    else:
        print(
            "il n'y a pas assez de quantité de {fruit} dans l'inventaire pour vendre {quantité} {fruit}"
        )


if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    prix = ouvrir_prix()
    afficher_inventaire(inventaire)
    afficher_tresorerie(tresorerie)
    recolter(inventaire, "bananes", 30)
    inventaire, tresorerie = vendre_fruits(inventaire, "bananes", 5, tresorerie, prix)

    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)
