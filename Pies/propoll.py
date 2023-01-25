file = "C:\\Users\\Abid Sheri\\Desktop\\Pies\\poll_results.txt"

active = True

with open(file, 'r') as ff:
    sho_f = ff.readlines()

num = 1

for l in sho_f:
    print(str(num) + '.', l)
    num += 1

while active:
    result = input("\nState reasons for loving programming. ")

    if result.upper() == 'STOP':
        break

    with open(file, 'a') as ff:
        ff.write('\n' + result)


