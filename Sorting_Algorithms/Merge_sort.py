#Merge Sort is a divide-and-conquer sorting algorithm.
#It divides an array into two halves, sorts them separately, and merges them.
#It's stable, efficient, and guarantees O(n log n) time complexity.
#Suitable for large datasets due to its consistent performance.

def merge_sort(arr):
    """
    Merge Sort is a divide-and-conquer algorithm that divides an array into two halves,
    recursively sorts them, and then merges the two sorted halves.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: A sorted list in ascending order.

    Examples:
    >>> merge_sort([38, 27, 43, 3, 9, 82, 10])
    [3, 9, 10, 27, 38, 43, 82]
    """
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
