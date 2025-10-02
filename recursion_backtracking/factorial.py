'''
Factorial of a number 'n' using recursion
Example:
Input:5
Output:120
'''

def facto(n):
    if n<0:
        return None
    if n<=1:
        return 1
    else:
        return n * facto(n-1)
     
        
n=int(input())
print(facto(n))
