failings={"1st":"Falsehood","2nd":"Slothfulness","3rd":"Perversion"}

print(failings)

failings.setdefault("4th","Rage")

print(failings)

print(failings.setdefault("4th","Envy"))

print(failings)

print(failings.get("5th","That's it"))

print(failings.get("6th","I assure you that those are all of them."))
