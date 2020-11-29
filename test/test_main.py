import pytest

from src.main import matrix_encode, matrix_decode, determinant_recursive, transpose_matrix, pad, determinant_recursive

def test_3():
    X = [[1,4,8],
    [3,7,2],
    [6,9,5]]

    A = [*("ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю")]
    A.sort()
    A.extend(['\n',' ','.',',',';',':','!','-'])
    print(A)

    plaintext = "Капабланка"
    det = determinant_recursive(X)    
    encoded_text = matrix_encode(X, A, plaintext)

    print(f"encoded_text: \n{encoded_text}")
    print("")

    T = transpose_matrix(X)
    
    print(f"T:")
    for r in T:
        print(r)

    print("")

    print(f"encoded_text: \n{encoded_text}")
    actual = matrix_decode(T, A, encoded_text, det)

    print(f"decoded_text: \n{actual}")
    assert actual == pad(X, "Капабланка")


def test_4():
    
    X = [[1,4,8,1],
        [3,7,2,1],
        [6,9,5,1],
        [1,2,3,4]]

    T = transpose_matrix(X)

    plaintext = """Любви, надежды, тихой славы
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

    print(f"T:")
    for r in T:
        print(r)

    print("")

    det = determinant_recursive(X)
    print(f"det: {det}")

    print("")

    encoded_text = matrix_encode(X, A, plaintext)
    print(f"encoded_text: \n{encoded_text}")
    print("")

    actual = matrix_decode(T, A, encoded_text, det)
    print(f"decoded_text: \n{actual}")
    print("")

    assert actual == pad(X, plaintext)

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