from random import randint as rr

from kryptor import pasNcrypt


def passgen():

    r = str(rr(0, 99))

    abet = 'A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z _'.split(' ')

    pass_pre = abet[rr(0, 52)]

    while len(pass_pre) < 8:
        pass_pre += abet[rr(0, 52)]

    pass_fin = pass_pre + r

    print('\nThe password', pass_fin, 'has been created for you.')

    #passf = pasNcrypt(pass_fin)

    return pass_fin


def passgen_p(p):

    r = str(rr(0, 99))

    abet = 'A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z _'.split(' ')

    pass_pre = abet[rr(0, 52)]

    while len(p) < 8:
        p += abet[rr(0, 52)]

    pass_fin = p + r

    print('\nThe password', pass_fin, 'has been created for you.')

    #passf = pasNcrypt(pass_fin)

    return pass_fin
