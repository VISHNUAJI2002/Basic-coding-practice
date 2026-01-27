"""
Problem Title: Matrix Multiplication

Description:
Given two matrices A and B, perform matrix multiplication and
print the resulting matrix.
Matrix multiplication is possible only if:
number of columns in A == number of rows in B.
If multiplication is not possible, print an appropriate message.

Example:
Input:
2 3
1 2 3
4 5 6
3 2
7 8
9 10
11 12

Output:
58 64
139 154

Explanation:
Matrix A is of size 2 × 3
Matrix B is of size 3 × 2

Result matrix size = 2 × 2
Each element is computed using row-by-column multiplication.
"""

def matrix_multiplication(A, B):
    rows_a = len(A)
    cols_a = len(A[0])
    rows_b = len(B)
    cols_b = len(B[0])

    # dimension validation
    if cols_a != rows_b:
        return None

    # preallocate result matrix
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += A[i][k] * B[k][j]

    return result


# -------------
# User Input
# -------------
r1, c1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(r1)]

r2, c2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(r2)]

result = matrix_multiplication(A, B)

if result is None:
    print("Matrix multiplication not possible")
else:
    for row in result:
        print(*row)
