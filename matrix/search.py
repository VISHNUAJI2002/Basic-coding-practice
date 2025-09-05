'''
Search an element in a matrix
Example:
Input:
2
3
1 2 3
4 5 6
5
Output:
True
'''

def search(x,m,n,t):
    l=0
    r=m*n -1
    while l<=r:
        mid=(l+r)//2
        row=mid//n
        col=mid%n
        midval=x[row][col]
        if midval==t:
            return True
        elif midval<t:
            l=mid+1
        else:
            r=mid-1
    return False        
        
    
    
rows=int(input())
cols=int(input())
matrix=[list(map(int,input().split())) for _ in range(rows)]
target=int(input())

print(search(matrix,rows,cols,target))
