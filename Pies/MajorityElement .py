def maj_elem(a):
	res, count = 0,0 # initialize count & result variables
	
	for i in a: # iterate over array
			if count == 0: # set element as result when count is 0
				res = i
			count += (1 if i == res else -1) # increment count whenever result occurs again else decrement
			
	if (a.count(res) > (len(a)//2)):
		return 1
	return 0
	
print(maj_elem([2,2,3,3]))
print(maj_elem([1,2,3,4]))
