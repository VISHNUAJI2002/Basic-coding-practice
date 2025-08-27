'''
You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
'''

def rotate(x):
    l=0
    r=len(x)-1
    while l<r:
        x[l],x[r]=x[r],x[l]
        l+=1
        r-=1
    for i in range(len(x)):
        for j in range(i,len(x)):
            x[i][j],x[j][i]=x[j][i],x[i][j]
    return x
    

rows = int(input("Enter number of rows: "))
matrix = [list(map(int, input().split())) for _ in range(rows)]

for i in rotate(matrix):
    print(i)
