# function to find the partition position
def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1

      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)
    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)

lis = []
n = int(input("Enter the length of array: "))
print("Enter "+str(n)+" elements")
for i in range(0, n):
    ele = int(input())
    lis.append(ele)

print("Unsorted Array")
print(lis)

quickSort(lis, 0, n-1)

print('Sorted Array in Ascending Order:')
print(lis)