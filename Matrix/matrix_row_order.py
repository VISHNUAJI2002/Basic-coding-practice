'''
Return True if all rows in a matrix that
are in non increasing order or non decreasing order.
Else False.
'''

def count1(matrix,m,n):
    totcount=0
    for i in range(m):
        asc=0
        desc=0  
        for j in range(1,n):
            if matrix[i][j]>=matrix[i][j-1]:
                asc+=1
            if matrix[i][j]<=matrix[i][j-1]:
                desc+=1
        if asc==n-1 or desc==n-1:
            totcount+=1
    return totcount==m
    
def count2(matrix,m,n):
    totcount=0
    for i in range(m):
        l=[]
        for j in range(n):
            l.append(matrix[i][j])
        if sorted(l)==l or sorted(l, reverse=True)==l:
            totcount+=1
    return totcount==m        
    
rows=int(input())
cols=int(input())
matrix=[list(map(int,input().split()))for _ in range(rows)]
print(count1(matrix,rows,cols))
print(count2(matrix,rows,cols))

'''
3 
4
5 5 8 9
2 2 2 2
9 8 7 6
True
True
'''

    
