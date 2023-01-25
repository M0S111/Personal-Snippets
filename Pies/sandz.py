sandwiches=["tuna","blt","pastrami","turkey","pastrami","grilled cheese","pastrami"]

done_sandwiches=[]

while sandwiches:

    while "pastrami" in sandwiches:
        sandwiches.remove("pastrami")
        print("Sorry, we are fresh out of pastrami.")

    processing=sandwiches.pop()
    done_sandwiches.append(processing)
    
    print("You're "+processing+" sandwich is done.")
   
if sandwiches==[]:
    print("\nAll orders completed.")
       
print("\nYou're orders were: ")

for d in done_sandwiches:
    print(d)
