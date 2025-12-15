inventaire = {
    "bananes": 150,
    "mangues": 85,
    "ananas": 45,
    "noix de coco": 60,
    "papayes": 30,
}


def afficher_inventaire(inventaire):
    print("l'inventaire actuel contient")
    for fruit, quantité in inventaire.items():
        print(f"{fruit.capitalize()} : {quantité} unités")


def recolter(inventaire, fruit, quantité):
    nouvelle_quantité = inventaire.get(fruit, 0) + quantité
    inventaire[fruit] = nouvelle_quantité
    print(f"nous avons recolté {quantité} {fruit} supplémentaire")


def vendre_fruits(inventaire, fruit, quantité):
    if inventaire.get(fruit, 0) >= quantité:
        inventaire[fruit] -= quantité
        print(f"Vendu: {quantité} unités de {fruit}")
    else:
        print(
            "il n'y a pas assez de quantité de {fruit} dans l'inventaire pour vendre {quantité} {fruit}"
        )


if __name__ == "__main__":
    afficher_inventaire(inventaire)
    recolter(inventaire, "bananes", 30)
    vendre_fruits(inventaire, "bananes", 5)
    afficher_inventaire(inventaire)
