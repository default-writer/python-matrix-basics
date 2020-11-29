X = [[1,4,8],
    [3,7,2],
    [6,9,5]]

def multiply(X, Y, det = 0):
    result = []
    for _ in range(len(X)):
        result.append(0)
    for i in range(len(X)):
        for j in range(len(X)):
            result[i] += X[i][j % len(X)] * Y[j]
    if det != 0:
        for i in range(len(X)):
            result[i] = int(result[i] / det)
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

text = """Любви, надежды, тихой славы
Недолго нежил нас обман,
Исчезли юные забавы,
Как сон, как утренний туман;
Но в нас горит еще желанье;
Под гнетом власти роковой
Нетерпеливою душой
Отчизны внемлем призыванье.
Мы ждем с томленьем упованья
Минуты вольности святой,
Как ждет любовник молодой
Минуты верного свиданья.

Пока свободою горим,
Пока сердца для чести живы,
Мой друг, отчизне посвятим
Души прекрасные порывы!
Товарищ, верь: взойдет она,
Звезда пленительного счастья,
Россия вспрянет ото сна,
И на обломках самовластья
Напишут наши имена!
"""

A = [*("ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю")]
A.sort()
A.extend(['\n',' ','.',',',';',':','!','-'])
print(A)

print("")

def encode(X, A, txt):
    result = []
    for i in range(len(txt)):
        result.append(A.index(txt[i]) + 1)
    return result

def decode(A, index):
    result = []
    for i in range(len(index)):
        result.append(A[index[i] - 1])
    return result

def pad(X, Y):
    if len(Y) % len(X) > 0:
        for _ in range(len(Y), len(Y) + len(X) - len(Y) % len(X), 1):
            Y += " "
    return Y


def matrix_encode(X, A, Y):
    result = []
    Y = pad(X, Y)
    if len(Y) % len(X) > 0:
        for i in range(len(Y), len(Y) + len(X) - len(Y) % len(X), 1):
            Y += " "
    for i in range(0, len(Y), len(X)):
        Y1 = encode(X, A, Y[i:i+len(X)])
        B1 = multiply(X, Y1)
        result.extend(B1)
    return result

def matrix_decode(X, A, Y, det):
    result = []
    for i in range(0, len(Y), len(X)):
        B1 = multiply(X, Y[i:i+len(X)], det)
        result.extend(B1)

    return "".join(decode(A, result))

T = transpose_matrix(X)

print(f"T:")
for r in T:
   print(r)

print("")

det = determinant_recursive(X)
print(f"det: {det}")

print("")

encoded_text = matrix_encode(X, A, text)
print(f"encoded_text: \n{encoded_text}")
print("")

print(f"decoded_text: \n{matrix_decode(T, A, encoded_text, det)}")
print("")

# print("enter text: ")
# lines = []
# while True:
#     line = input()
#     if line:
#         lines.append(line)
#     else:
#         break
# text = '\n'.join(lines)

# encoded_text = matrix_encode(X, A, text)
# print(f"encoded_text: \n{encoded_text}")
# print("")

# print(f"decoded_text: \n{matrix_decode(T, A, encoded_text, det)}")
# print("")