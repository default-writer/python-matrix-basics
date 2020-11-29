import pytest

from src.main import X, A, text, matrix_encode, matrix_decode, determinant_recursive, transpose_matrix, pad

def test_main():
    det = determinant_recursive(X)    
    encoded_text = matrix_encode(X, A, text)

    print(f"encoded_text: \n{encoded_text}")
    print("")

    T = transpose_matrix(X)

    print(f"encoded_text: \n{encoded_text}")
    actual = matrix_decode(T, A, encoded_text, det)

    print(f"decoded_text: \n{actual}")
    assert actual == pad(X, text)
