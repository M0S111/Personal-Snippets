from random import randint as rn


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def rollDie(self):
        roll = rn(1, self.sides)
        return roll


rollt = []

play = True

while play:

    d = Die()

    dr = d.rollDie()

    rollt.append(dr)

    total = 0

    print("\nYou rolled a", dr)

    q = input("\nDo you want to roll or pass? (P to pass) ")

    if q.upper() == 'P':

        play = False

        for r in rollt:
            total = total + r

        print("\nYour total is", total)
