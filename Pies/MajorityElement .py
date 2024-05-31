def maj_elem(a):
	res, count = 0,0
	
	for i in a:
			if count == 0:
				res = i
			count += (1 if i == res else -1)
			
	if (a.count(res) > (len(a)//2)):
		return 1
	return 0
	
print(maj_elem([2,3,9,2,2]))
print(maj_elem([1,2,3,4]))