# Peak finder algorithm design & analysis

myray = [5, 3, 8, 13, 46, 2, 9, 239, 10]

#while myray:
    #print("\n",max(myray))
    #popit = myray.index(max(myray))
    #myray.pop(popit)

check = 0

for i in myray:
    if i > check:
        check = i
print("\n",check)
