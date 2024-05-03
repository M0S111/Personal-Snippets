def recurCount(arr):

	if len(arr) == 1: # base case with 1 element in array
		return 1

	arr.pop() # counting down by removing element at end
	count = len(arr) - (len(arr) - 1) # count found by subtracting length of array - 1 from length equaling 1

	return count + recurCount(arr) # count incremented recursively

print(recurCount([4,6,7,2,4,5,9,8,5,6,3,5,4,8,2,5,9,4,7,5,6,8,6,9,5]))