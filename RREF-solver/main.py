# please don't write no of columns and no of rows as input at starting in my text file i make wrote
# code in such a way that it takes only pure matrix i already provided samply clear sample and
# put your own for working. Thank You.

# note: if any value in my rref in comes in e form like 1.4210854715202004e-14 consider it zero as it too small and your output takes it as zero

# taking input from other files
matrix = []
file = open("matrixInput.txt", "r")
matrix_input = [i.strip() for i in file.readlines()]
for i in matrix_input:
    l = i.split(" ")
    l2 = [int(j) for j in l]
    matrix.append(l2)


# e used for base condition
e = 0

# subtract function will subtract all elements below pivot and also act as base condition to stop the loop when we all get all pivot

def subtract(matrix,n,m):
    d = matrix[n]
    for ind, rows in enumerate(matrix):
        if ind != n:
            if rows[m] != 0:
                c = rows[m]
                for ind2, rowsElement in enumerate(rows):
                    rows[ind2] = rows[ind2] - (d[ind2] * c)
    if len(matrix) >= len(matrix[0]):       #to check whether no of rows of matrix is greater than or equal no of columns i did it to stop when all pivot position found
        if n != len(matrix[0]) - 1:
            func(n+1)
        return
    elif len(matrix[0]) > len(matrix):
        if n != len(matrix)-1:
            func(n+1)
        return

# func3 for this when this situation comes 1 2 0 4
#                                          0 0 4 5
#                                          0 0 2 1
#                                          0 0 0 5
# here colm 2 has all zeros so it goes for col3 -> func3 do this

def func3(n,m):
    count = 0
    for ind , rows in enumerate(matrix):
        if m > len(matrix[0])-1: break
        if ind >= n and matrix[n][m] != 0 :
            c = rows[m]
            for ind2, rowsElement in enumerate(rows):
                rows[ind2] = rowsElement/c
            return subtract(matrix, n,m)
        elif ind >= n and matrix[n][m] == 0:
            a = matrix[n]
            if rows[m] != 0:
                d = rows[m]
                for ind3, rowsElement3 in enumerate(rows):
                    matrix[ind][ind3] = rowsElement3/d
                matrix[n] = matrix[ind]
                matrix[ind] = a
                return subtract(matrix,n,m)
        if ind>=n and matrix[n][m] == 0: count+=1
    if count == len(matrix) - n:
        return func3(n,m+1)

# func will make rows first element 1 by dividing all element by that number if first element in 0 then interchange with another row whose first element is not 1 if all
# have 0 then it will call func3
def func(e):
    count = 0
    for ind, rows in enumerate(matrix):
        # if matrix(1,1) is 0
        if ind > e and matrix[e][e] == 0:                                           # ind isliye lagaya ha taki o ke niche wale row ko le sake
            a = matrix[e]
            if rows[e] != 0:
                matrix[e] = matrix[ind]                                             #to change 0 coefficient rows with non zero coefficient rows
                matrix[ind] = a
                # now make all rows first element coefficient 1
                for ind2, rows2 in enumerate(matrix):
                    if ind2 == e:
                        b = rows2[e]
                        if b != 0:
                            for ind3, rowsElement in enumerate(rows2):
                                if ind3 >= e:
                                    matrix[ind2][ind3] = rowsElement / b

                        break
                return subtract(matrix,e,e)

        elif matrix[e][e] != 0:
            for ind4, rows4 in enumerate(matrix):
                if ind4 >= e:
                    b = rows4[e]
                    if b != 0:
                        for ind5, rowsElement in enumerate(rows4):
                            if ind5 >= e:
                                matrix[ind4][ind5] = rowsElement / b
                    break
            return subtract(matrix,e,e)
        if ind>=e:
            if rows[e] == 0: count+= 1
    if count == len(matrix) - e:
        return func3(e,e+1)
func(e)
# printing rref in 2d form
print(f"The rref form is: ")
for i in matrix:
    for j in i: print(float(j),end="  ")
    print()

colmns = len(matrix[0])
rows = len(matrix)
pivotPosition = []

# functino for determining pivot position
def pivot(n,m):
    if m < colmns:
        a = False
        for i in range(n,len(matrix)):
            if matrix[n][m] == 1:
                a = True
        if a:
            pivotPosition.append((n,m))
            pivot(n+1,m+1)
        else:
            pivot(n,m+1)
pivot(0,0)
print()
print(f"The pivot position is: {pivotPosition} ")
basicvariable = [j for i,j in pivotPosition ]
freevariable = [i for i in range(colmns) if i not in basicvariable]

def generalSolution():
    lst1 = []
    a = 0
    for i in range(colmns):
        d = {}
        if i in basicvariable:
            for j in range(colmns):
                if i != j and matrix[a][j] !=0:
                    d[j] = -abs(matrix[a][j]) if matrix[a][j] > 0 else abs(matrix[a][j])
            a+=1
        else: d[i] = 1
        lst1.append(d)
    lst2 = [[items.get(k) if items.get(k)!= None else 0 for items in lst1 ] for k in freevariable]
    return lst2
lst2 = generalSolution()
print()
print("The general solution is:")
print([0]*colmns,end="+")
for i in range(len(freevariable)):
    if i == len(freevariable)-1: print(f"x_{freevariable[i]} *{lst2[i]}")
    else: print(f"x_{freevariable[i]} *{lst2[i]}",end="+")