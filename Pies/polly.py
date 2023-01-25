ans = {}

poll_active = True

while poll_active:
    n = input("\nPlease, enter name. ")
    a = input("\nIf you could visit one place in the world, where would you go? ")
    ans[n] = a

    repeat = input("\nWould you like to let another person respond? (y/n) ")

    if repeat.lower() == 'n':
        break
    else:
        continue

for n, a in ans.items():
    print("\n", n.title() + " would like to see " + a.title() + ".")

