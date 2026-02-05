"""
Problem Title: Matrix Subtraction with Dimension Validation

Description:
Given two matrices A and B, subtract matrix B from matrix A
and print the resulting matrix.
Matrix subtraction is possible only if:
both matrices have the same number of rows and columns.
If subtraction is not possible, print an appropriate message.

Example:
Input:
2 2
5 6
7 8
2 2
1 2
3 4

Output:
4 4
4 4

Explanation:
Matrix A:
5 6
7 8

Matrix B:
1 2
3 4

Result matrix is obtained by subtracting
each element of B from the corresponding element of A.
"""

def matrix_subtraction(A, B):
    rows_a = len(A)
    cols_a = len(A[0])
    rows_b = len(B)
    cols_b = len(B[0])

    # dimension validation
    if rows_a != rows_b or cols_a != cols_b:
        return None

    # preallocate result matrix
    result = [[0 for _ in range(cols_a)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_a):
            result[i][j] = A[i][j] - B[i][j]

    return result



r1, c1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(r1)]

r2, c2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(r2)]

result = matrix_subtraction(A, B)

if result is None:
    print("Matrix subtraction not possible")
else:
    for row in result:
        print(*row)
