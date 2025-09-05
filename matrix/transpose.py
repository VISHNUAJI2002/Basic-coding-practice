'''
Transpose of given matrix
Example:
Input:
2
3
4 5 6 
1 2 3
Output:
[4, 1]
[5, 2]
[6, 3]
'''

def transpose_sqr(x):    #for square matrices
    n=len(x)
    for i in range(n):
        for j in range(i+1,n):
            x[i][j],x[j][i]=x[j][i],x[i][j]
    return x

def transpose_rect(matrix,m,n):   #for rectangular matrices
    transposed=[[0]*m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            transposed[j][i]=matrix[i][j]
    return transposed
    
    
rows=int(input())
cols=int(input())
matrix=[list(map(int,input().split()))for _ in range(rows)]

if rows==cols:   # square matrix
    result=transpose_sqr(matrix)
else:              # rectangular matrix
    result=transpose_rect(matrix, rows, cols)

for i in result:
    print(i)
    
