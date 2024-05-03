def recurSum(arr):

	if len(arr) == 0: # base case when array is empty
		return 0

	elif len(arr) == 1: # base case when array has 1 element
		return arr[0]

	first = arr.pop(0) # recursion starts here with seperating first element of array

	return first + recurSum(arr) # & then summing it with rest of array recursively

print(recurSum([4,6,8]))
