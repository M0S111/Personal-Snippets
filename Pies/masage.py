import random

tipsy=random.randrange(7,9)

_winner="   Winner, winner\n\t chicken dinner!   "
winner_prop=_winner.strip()

answer=int(input("Guess number & win!"))


if answer==tipsy:
    print(winner_prop.upper())
else:
    print("LOSER!!!")


if answer>=13 or answer==7:
    print("Bumper Prize!!!")
else:
    print("DOUBLE BOKE!!!")
