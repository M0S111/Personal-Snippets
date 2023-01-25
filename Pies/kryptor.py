def pasNcrypt(passw):

    key = 256
    newp = []

    while key == 256:
        key = int(input("\nPlease enter a valid numerical key for encryption: "))

    for i in range(len(passw)):

        z = ord(passw[i])

        z = z ^ key

        z = chr(z)

        newp.append(z)

    np_fin = "".join(newp)

    return np_fin


def pasDcrypt(passw, key):

    newp = []

    for i in range(len(passw)):

        z = ord(passw[i])

        z = z ^ key

        z = chr(z)

        newp.append(z)

    np_win = "".join(newp)

    return np_win