def binarysearch(array1, number, beg, end):
    array = sorted(array1)
    print("Binary Search: ",array)

    while True:
    
        mid = int((beg + end)/2)

        if array[mid] == number:
            return mid
        elif array[mid] < number:
            beg = mid + 1
        elif array[mid] > number:
            end = mid - 1

# Linear Search
def linearsearch(array, number):
     print("Linear Search: ",array)
     for i in range(0,len(array)):
          if array[i] == number:
               return i
          else:
               pass 

list = []
n = int(input("Enter number of elements : "))

print("Enter ",n," elements")
for i in range(0, n):
	ele = int(input())
	list.append(ele)

beg = 0
end = len(list) - 1
number = int(input("Enter the element to search: ")) 

resultbs = binarysearch(list, number, beg, end)

if resultbs:
    print("Element is present at index ", resultbs)
else:
    print("Element not found")

# resultls = linearsearch(list, number)

# if resultls:
#     print("Element is present at index ", resultls)
# else:
#     print("Element not found")    