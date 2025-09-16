'''
Diamond (stars)

Example:
Input:
4
Output:
   *
  ***
 *****
*******
 *****
  ***
   *
'''

def diamond(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"*" * (2*i-1))
    for i in range(n-1,0,-1):
        print(" "* (n-i)+"*"*(2*i-1))
        
n=int(input())
diamond(n)
