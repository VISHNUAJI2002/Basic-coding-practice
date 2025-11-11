'''
Matrix Addition.
Given two matrices of the same dimensions, find their sum.

The sum of two matrices A and B of the same dimension m×n 
is a matrix C where each element is calculated as:
C[i][j] = A[i][j] + B[i][j]

Example:
Input:
Enter rows and columns: 3 3
Enter first matrix:
1 2 3
4 5 6
7 8 9
Enter second matrix:
9 8 7
6 5 4
3 2 1

Output:
Sum of matrices:
10 10 10
10 10 10
10 10 10
'''

def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices must have the same dimensions for addition"

    rows = len(mat1)
    cols = len(mat1[0])
    result = [[0] * cols for _ in range(rows)] 

    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] + mat2[i][j]

    return result


rows, cols = map(int, input("Enter rows and columns: ").split())
print("Enter first matrix:")
mat1 = [list(map(int, input().split())) for _ in range(rows)]
print("Enter second matrix:")
mat2 = [list(map(int, input().split())) for _ in range(rows)]


result_matrix = add_matrices(mat1, mat2)
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Sum of matrices:")
    for row in result_matrix:
        print(*row)
