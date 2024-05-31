def quicksort(arr):
 if len(arr) <= 1:
  return arr
 else:

  pivot = arr[0]

  left = [x for x in arr if x < pivot]
  right = [x for x in arr if x > pivot]
  equal = [x for x in arr if x == pivot]

  return quicksort(left) + equal + quicksort(right)
  
a = [2,3,9,2,2,9,3,-20,0,-2]
b = [2]
c = [5,6,6,8,9,13]
a.reverse()
print(a)
print(quicksort(a))