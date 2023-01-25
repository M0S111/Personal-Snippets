try:

    with open(r'C:\Users\Abid Sheri\Desktop\Pies\Form Content.txt') as fc:
        a = fc.read()
        print(a.strip())

except FileNotFoundError:
    print("\nFile not located!")
