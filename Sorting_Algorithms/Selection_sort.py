#Selection sort
#Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process continues until no swaps are needed, indicating the list is sorted.

#The algorithm iterates through the list for 'n' elements (length of the list).
#Within each iteration, it compares adjacent elements from the beginning of the list to the (n - i - 1)-th element.
#If an element is greater than the one next to it, a swap is performed.
#This process is repeated until the largest unsorted element "bubbles up" to its correct position at the end of the list.
#The next iteration is then performed on the remaining unsorted portion.
#The process repeats until no more swaps are needed, indicating the list is sorted.
#Bubble Sort is inefficient for large lists but is easy to understand and implement.
#It has a time complexity of O(n^2) in the worst case, making it impractical for large datasets.

def selection_sort(arr):
    """
    Sort a list using Selection Sort.

    >>> selection_sort([4, 2, 7, 1, 9, 3])
    [1, 2, 3, 4, 7, 9]

    >>> selection_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
