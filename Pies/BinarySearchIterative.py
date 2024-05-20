# Uses python3
import sys

def binary_search(a, x):

 left, right = 0, len(a) - 1
 
 if (x < (a[0])) or (x > (a[-1])):
   return -1
 
 while (left <= right):

  mid = ((right + left)//2)
  
  if (x < a[mid]):
   right = mid - 1
   
  elif (x > a[mid]):
   left = mid + 1

  else:
      return mid
   
 return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    a.sort()
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
