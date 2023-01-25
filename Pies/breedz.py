import os


def petfile(name):

    try:
        with open(name, 'r') as fn:
            f = fn.read()

    except FileNotFoundError:
        # pass
        print('\nSorry. The file is missing.')

    try:
        if os.path.basename(name) == "Cats.txt":
            print('\nA few cat breeds:\n', f)

        else:
            print('\nA few dog breeds:\n', f)

    except UnboundLocalError:
        # pass
        print("\nContents of missing file can't be printed.")


file_c = "C:\\Users\\Abid Sheri\\Desktop\\Pies\\DataStore\\Cats.txt"
file_d = "C:\\Users\\Abid Sheri\\Desktop\\Pies\\DataStore\\Dogs.txt"

petfile(file_c)

petfile(file_d)
