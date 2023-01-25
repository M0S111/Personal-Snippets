kars=["Merc","Subaru","Toyota","Honda","Seat"]

want=input("Pick rental brand. ")

want_fin=want.title()

if want_fin in kars:
    print("Let's get you that "+want_fin+".")
else:
    print("We don't have a "+want_fin+" for you. \nSorry.")
