#simple number pyramid

def numpyramid(n):
    for i in range(1,n+1):
        print(" "*(n-i),end=" ")
        print((str(i)+" ")*i)
        
n=int(input())   
numpyramid(n)
