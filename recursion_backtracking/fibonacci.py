'''
Fibonacci sequence using recursion
Example:
Input: 6
Output: 0 1 1 2 3 5
'''

def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        

n=int(input())
for i in range(n):
    print(fibonacci(i), end=" ")
    
