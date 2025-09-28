'''
Fibonacci series
Example:
Input:10
Output:0 1 1 2 3 5 8 13 21 34 
'''

def fibonacci(n):
    a=0
    b=1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b
        
n=int(input())
fibonacci(n)
