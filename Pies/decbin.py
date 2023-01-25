import copy

def BinDec(b_num):

    exp = len(b_num) - 1

    tot = 0

    for i in b_num:
        
        count = int(i) * (2 ** exp)

        tot += count

        print("\nThe product of", i,"multiplied by 2 to the", exp,"is", count)

        exp -= 1

    conc = print("\nThe decimal form of", b_num, "is:", tot)
    
    return conc


def DeciBin(d_num):
    
    dec = d_num

    d_num = int(d_num)

    remain = []

    while d_num > 0:

        remain.append(str(d_num % 2))

        bin_l = copy.copy(remain)

        r_f = reversed(remain)

        print("\nThe remainder of", d_num, "divided by 2 is", bin_l.pop(), "\nThe quotient is", d_num // 2)

        d_num = d_num // 2

    conc = print("\nThe binary form of", dec, "is:", "".join(r_f))

    return conc

##def Comple(num =(input("\nState binary number for conversion. "))):
##
##    comped = []
##
##    for i in num:
##
##        n = not int(i)
##
##        comped.append(int(n))
##
##    print(comped)

check = int(input("Choose function: 1 for binary to decimal, anything else for decimal to binary. " ))

if check == 1:

    n = input("\nState binary number for conversion. ")
    BinDec(n)

else:
    
    n = input("\nState decimal number for conversion. ")
    DeciBin(n)

#Comple()
