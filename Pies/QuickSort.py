a = [2,3,9,2,2,10,5,44,41,50,11,12,12,66,101,97,5,92,87,42,46]

def partition(A,l,r):
    
    pivot = A[l]
    
    j = l #points to first element of array

    for i in range(l+1,r+1):#start from l+1 cus j is l
        
        if A[i] <= pivot:
            j += 1 #increment j when A[i] is smaller than pivot to add it to less than region from j to i
            
            (A[i],A[j]) = (A[j],A[i]) #place element smaller than pivot (A[i]) on left of pivot by swapping with leftmost element (A[j])
            
    (A[l],A[j]) = (A[j],A[l]) #swap current pivot at A[l] with A[j] to place pivot in sorted position
        
    return j #return partitioning index
    
def Qsort(A,l,r):
    if (l >= r):
            return A
    else:
        pivot_index = partition(A,l,r)
        Qsort(A,l,pivot_index -1)
        Qsort(A,pivot_index +1,r)


Qsort(a,0,len(a)-1)        
print(a)
