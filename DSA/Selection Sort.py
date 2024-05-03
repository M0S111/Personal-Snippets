def findSmallest(arr):

	least = arr[0]

	for i in arr: 

		if least > i :

			least = i


	return least



def SelectionSort(arr):
	
	sorted = []

	while len(arr) != 0:
		smallest = min(arr)
		index = arr.index(smallest)
		sorted.append(smallest)
		arr.pop(index)

	return sorted

myArray = [47,89,46,7,100,55,63,11]

print(findSmallest(myArray))

print(SelectionSort(myArray))