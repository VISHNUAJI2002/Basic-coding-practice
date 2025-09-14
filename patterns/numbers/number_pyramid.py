'''
simple number pyramid
Example:
Input:
5
Output:
     1 
    2 2 
   3 3 3 
  4 4 4 4 
 5 5 5 5 5
 
 '''

def numpyramid(n):
    for i in range(1,n+1):
        print(" "*(n-i),end=" ")
        print((str(i)+" ")*i)
        
n=int(input())   
numpyramid(n)
