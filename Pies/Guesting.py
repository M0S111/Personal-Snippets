fn = r"C:\Users\Abid Sheri\Desktop\Pies\Guestbook.txt"

choice = input("\nSelect an option. V to view Guestbook or R to register. ")

if choice.upper() == 'R':

    name = input("\nYour name please. ")
    print("\nHello & welcome", name.title() + '.')

    with open(fn, 'a') as f:
        f.write("\n" + name.title())

    print("You have been successfully registered.")

    with open(fn, 'r') as f:
        re = f.read()
        print("\nCurrently registered guests:", re + ' <= You')

else:

    with open(fn, 'r') as f:
        re = f.read()
        print("\nCurrently registered guests:", re)
