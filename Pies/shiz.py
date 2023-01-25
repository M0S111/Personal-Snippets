shit = {"Bachelors degrees": 4, "PhDs": 2, "Technical certificates": 5}


def displaycheevos(lizt):
    print("Your cheevos:")
    total_cheevez = 0
    for i, v in lizt.items():
        print("You have", v, i)
        total_cheevez += v
    print("\nYour total cheevez r:" + "\n", total_cheevez)


displaycheevos(shit)


