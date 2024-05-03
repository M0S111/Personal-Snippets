def binarySearch(arr,item):

	arr.sort() # sort array if unsorted

	orig = arr

	mid = (len(arr) // 2) # initially assign middle

	while (item != (arr[mid])): # start loop to find item

		if item == (arr[mid]): # if found exit
			break

		elif (len(arr) == 1) and (item != (arr[mid])):
			return f"\'{item}\' not in ordered array: {orig}"

		elif item > (arr[mid]): # if item is bigger than middle element in ordered array update array to start from there & change mid to be middle of new array
			arr = arr[mid+1:len(arr)]
			mid = (len(arr) // 2)
			print(arr,'\n')

		else: # if item is less than middle element in ordered array update array to end there & change mid to be middle of new array
			arr = arr[0:mid]
			mid = (len(arr) // 2)
			print(arr,'\n')


	res = orig.index(arr[mid]) # get pos in original ordered array

	return f"\'{item}\' found at index position {res} in ordered array: {orig}"

print(binarySearch([556,87,78,654,165,48,79,87,455,6,66,19,70],79))