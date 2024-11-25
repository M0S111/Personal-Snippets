def CountSort(arr):
    count = [0]*((max(arr))+1)
    fin = []

    for i in range(len(count)):
        count[i] = arr.count(i)

    for i in range(len(count)):
        if count[i] > 0:
            while count[i] != 0:
                
                fin.append(i)
                count[i]-=1

    return fin

def count_sort(arr):
    max_val = max(arr)
    count_arr = [0] * (max_val + 1)

    # Count the occurrence of each number in the array
    for num in arr:
        count_arr[num] += 1

    sorted_arr = []
    # Reconstruct the sorted array using the count array
    for i, count in enumerate(count_arr):
        sorted_arr.extend([i]*count)

    return sorted_arr



print([2,6,4,9,2,4])
print(count_sort([2,6,4,9,2,4]))
