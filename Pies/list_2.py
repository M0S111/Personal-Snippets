guests=[]

guests.append("Newton")
guests.append("Einstein")
guests.append("Turing")

for n in guests:
    print("I cordially invite",n +".\n")

not_polite=guests.pop(0)

print(not_polite,"ain't comin'\n")

guests.insert(0,"Hooke")

for n in guests:
    print("\tI now cordially invite",n +".\n")

num_guest=len(guests)
num_final=str(num_guest)

print("We have invited "+num_final+" guests.")

print("I think",len(guests),"is enough.")
