import json


def ouvrir_inventaire(path="data/inventaire.json"):
    with open(path, "r", encoding="utf-8") as fichier:
        inventaire = json.load(fichier)
    return inventaire


def ecrire_inventaire(inventaire, path="data/inventaire.json"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)


def ouvrir_tresorerie(path="tresorerie.txt"):
    with open(path, "r", encoding="utf-8") as fichier:
        tresorerie = json.load(fichier)
    return tresorerie


def ecrire_tresorerie(tresorerie, path="tresorerie.txt"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(tresorerie, fichier, ensure_ascii=False, indent=2)


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


def vendre_fruits(inventaire, fruit, quantité, tresorerie):
    if inventaire.get(fruit, 0) >= quantité:
        inventaire[fruit] -= quantité
        ecrire_inventaire(inventaire)
        tresorerie += 1 * quantité
        print(f"Vendu: {quantité} unités de {fruit}")
        return (inventaire, tresorerie)
    else:
        print(
            "il n'y a pas assez de quantité de {fruit} dans l'inventaire pour vendre {quantité} {fruit}"
        )


if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    afficher_inventaire(inventaire)
    afficher_tresorerie(tresorerie)
    recolter(inventaire, "bananes", 30)
    inventaire, tresorerie = vendre_fruits(inventaire, "bananes", 5, tresorerie)

    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)
