
run=True

while run==True:
    try:
        val_nu=int(input("\nProvide numerical input. "))
        mul=val_nu//10

    except ValueError:
        print("\nBAD INPUT!!! Only integers are valid.")

    if val_nu%10!=0:
        print("\nSorry. This isn't a multiple of 10. Try again.")

    elif val_nu%10==0:
        val_fin=str(val_nu)
        print("\nCongrats. This is a multiple of 10.\n",mul,"times 10 is "+val_fin+".")
        run=False


