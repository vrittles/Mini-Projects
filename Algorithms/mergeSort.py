def mergeSort(array):
    if len(array) > 1:

        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == '__main__':
    

    lis = []
    n = int(input("Enter the length of array: "))
    print("Enter "+str(n)+" elements")
    for i in range(0, n):
        ele = int(input())
        lis.append(ele)
    
    print("Unsorted array is: ")
    printList(lis)
    
    mergeSort(lis)

    print("Sorted array is: ")
    printList(lis)