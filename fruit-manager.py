import json


def ouvrir_inventaire(path="inventaire.json"):
    with open(path, "r", encoding="utf-8") as fichier:
        inventaire = json.load(fichier)
    return inventaire


def ecrire_inventaire(inventaire, path="inventaire.json"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)


def afficher_inventaire(inventaire):
    print("l'inventaire actuel contient")
    for fruit, quantité in inventaire.items():
        print(f"{fruit.capitalize()} : {quantité} unités")


def recolter(inventaire, fruit, quantité):
    nouvelle_quantité = inventaire.get(fruit, 0) + quantité
    inventaire[fruit] = nouvelle_quantité
    ecrire_inventaire(inventaire)
    print(f"nous avons recolté {quantité} {fruit} supplémentaire")


def vendre_fruits(inventaire, fruit, quantité):
    if inventaire.get(fruit, 0) >= quantité:
        inventaire[fruit] -= quantité
        ecrire_inventaire(inventaire)
        print(f"Vendu: {quantité} unités de {fruit}")
    else:
        print(
            "il n'y a pas assez de quantité de {fruit} dans l'inventaire pour vendre {quantité} {fruit}"
        )


if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    afficher_inventaire(inventaire)
    recolter(inventaire, "bananes", 30)
    vendre_fruits(inventaire, "bananes", 5)
    afficher_inventaire(inventaire)
