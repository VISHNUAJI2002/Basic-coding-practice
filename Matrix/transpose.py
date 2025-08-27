#Transpose of given matrix

def transpose(x):
    n=len(x)
    for i in range(n):
        for j in range(i+1,n):
            x[i][j],x[j][i]=x[j][i],x[i][j]
    return x
    
    
rows=int(input("no. of rows:"))
matrix=[list(map(int,input().split())) for _ in range(rows)]

for i in transpose(matrix):
    print(i)
