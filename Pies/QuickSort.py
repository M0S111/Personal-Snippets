a = [2,3,9,2,2]

def partition(A,l,r):
	pivot = A[r]
	
	i = l-1 #points to last element of array

	for j in range(l,r):
		
		if A[j] <= pivot:
			i += 1 #points to first element of array
			
			(A[i],A[j]) = (A[j],A[i]) #place element smaller than pivot (A[j]) on left of pivot by swapping with leftmost element (A[i])
			
	(A[i+1],A[r]) = (A[r],A[i+1]) #swap current pivot at A[r] with A[i+1] to place pivot in sorted position
		
	return i+1 #return partitioning index
	
def Qsort(A,l,r):
	if (l < r):
		pivot_index = partition(A,l,r)
		Qsort(A,l,pivot_index -1)
		Qsort(A,pivot_index +1,r)


Qsort(a,0,4)		
print(a)
