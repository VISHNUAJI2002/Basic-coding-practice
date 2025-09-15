'''
Continuous Numbers Pyramid.
Example:
Input:
4
Output:
   1 
  2 3 
 4 5 6 
7 8 9 10 

'''

def continuous_numpyramid(n):
    num = 1
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        for j in range(1, i+1):
            print(num, end=" ")
            num += 1
        print()
    
n=int(input())
continuous_numpyramid(n)
