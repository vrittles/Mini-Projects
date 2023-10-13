#Heap Sort
#Heap Sort is an in-place, comparison-based sorting algorithm.
#It first transforms the array into a max-heap, then repeatedly extracts the maximum element, leading to a sorted list.
#It offers consistent O(n log n) time complexity but is not stable.
#It's practical for sorting large datasets in memory-constrained environments.

def heap_sort(arr):
    """
    Sorts a list using the Heap Sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: A sorted list in ascending order.

    Examples:
    >>> heap_sort([38, 27, 43, 3, 9, 82, 10])
    [3, 9, 10, 27, 38, 43, 82]
    >>> heap_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> heap_sort([])
    []
    """

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            heapify(arr, n, largest)

    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
heap_sort(arr)
print(arr)
