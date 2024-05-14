# Max/Min finder algorithm design & analysis

myray = [57, 39, 8, 1307, 466, 22, 9, 239, 10]

#while myray:
    #print("\n",max(myray))
    #popit = myray.index(max(myray))
    #myray.pop(popit)

check = 0 # check var is assigned current greatest value in array

for i in myray: # iterate over length of array
    if i > check: # if current value is greater than previous
        check = i # assign to check
print("\n",check) # end for loop, print max value

###################################################################

least = myray[0] # initialize least var to hold val at index 0

for i in myray: # iterate over length of array
    if i < least: # if current value is less than previous
        least = i # assign to least
print("\n",least) # end for loop, print min value
        
