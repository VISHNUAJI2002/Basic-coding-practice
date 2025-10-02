'''
Sum of first n natural numbers using recursion.
Example:
Input: 5
Output: 15
Explanation: 1 + 2 + 3 + 4 + 5 = 15
'''

def sum_natural(n):
    if n <= 0:
        return 0  
    return n + sum_natural(n-1)  

n=int(input())
print(sum_natural(n))
