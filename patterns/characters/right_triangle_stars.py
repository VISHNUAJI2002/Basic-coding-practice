'''
Right-angled triangle using *

Example:
Input:
5
Output:
*
**
***
****
*****
'''

def rightTriangle(n):
    for i in range(1, n+1):
        print("*" * i)
        
        
n=int(input())
rightTriangle(n)
