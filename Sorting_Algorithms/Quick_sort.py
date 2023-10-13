#Quick Sort
#Quick Sort is a fast and efficient divide-and-conquer sorting algorithm.
#It selects a "pivot" element, partitions the array into two sublists (less and greater than the pivot), and recursively sorts them.
#It's not stable but offers average-case time complexity of O(n log n).
#It's widely used and performs well in practice.

def quick_sort(arr):
    """
    Sorts a list using the Quick Sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: A sorted list in ascending order.

    Examples:
    >>> quick_sort([38, 27, 43, 3, 9, 82, 10])
    [3, 9, 10, 27, 38, 43, 82]
    >>> quick_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> quick_sort([])
    []
    """

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose the pivot element

    # Partition the array into elements less than and greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the sublists and concatenate them
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print(sorted_arr)
