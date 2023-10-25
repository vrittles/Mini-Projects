def selectionSort(array, size):
   
    for ele in range(size):
        min_idx = ele

        for i in range(ele + 1, size): 
            if array[i] < array[min_idx]:
                min_idx = i

        (array[ele], array[min_idx]) = (array[min_idx], array[ele])

lis = []
n = int(input("Enter the length of array: "))
print("Enter "+str(n)+" elements")
for i in range(0, n):
    ele = int(input())
    lis.append(ele)

selectionSort(lis, n)
print('Sorted Array in Ascending Order:')
print(lis)