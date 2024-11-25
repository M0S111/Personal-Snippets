def heapify(array, n, i, swaps):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] < array[smallest]:
        smallest = left

    if right < n and array[right] < array[smallest]:
        smallest = right

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        swaps.append((i, smallest))
        heapify(array, n, smallest, swaps)

def buildHeap(array):
    n = len(array)
    swaps = []

    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i, swaps)

    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

# Example usage
buildHeap([5, 4, 3, 2, 1])
