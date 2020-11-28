X = [[1,4,8],
    [3,7,2],
    [6,9,5]]

Y1 = [8, 1, 2]
Y2 = [1, 3, 1]

def multiply(X, Y, det = 0):
    result = []
    for k in range(len(Y)):
        result.append(0)
    for i in range(len(X)):
        for j in range(len(Y)):
            result[i] += X[i][j] * Y[j]
    if det != 0:
        for i in range(len(Y)):
            result[i] = int(result[i] / det);
    return result

def submatrix(A, x, y):
    result = []
    for i in range(len(X)):
        if i != x:
            row = []
            for j in range(len(X[i])):
                if j != y:
                    row.append(X[i][j])
            result.append(row)
    return result

def copy_matrix(A):
    from copy import deepcopy
    return deepcopy(A)

def determinant_recursive(A, total=0):
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    for i in range(len(A)):
        for j in range(len(A[i])):
            sign = (-1) ** (i % 2) 
            sub_det = determinant_recursive(submatrix(A, i, j))
            total += sign * A[i][j] * sub_det
    return total

def transpose_matrix(A):
    determinant = determinant_recursive(A)
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            Aji = (-1)**(i + j) * determinant_recursive(submatrix(A, j, i))
            Aji / determinant
            row.append(Aji)
        result.append(row)
    return result

print(Y1)
print(Y2)

B1 = multiply(X, Y1)
B2 = multiply(X, Y2)

print(B1)
print(B2)

det = determinant_recursive(X)
print(det)

T = transpose_matrix(X)
for r in T:
   print(r)

print(multiply(T,B1,det))
print(multiply(T,B2,det))