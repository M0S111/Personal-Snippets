lizards=[t**3 for t in range(0,20,2)]
print(lizards)
print(type(lizards))
print(lizards.index(1728))

for l in lizards:
    lizards.pop(-1)
    print(l)

bats=[b-1 for b in range(3,15,3)]
print(bats)


print(lizards==bats)

