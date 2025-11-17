'''
Write a Python program to check a number is pronic number.

A pronic number, also known as an oblong number or rectangular number, is a type of
figurate number that represents a rectangle. It is the product of two consecutive integers, n
and (n + 1). Mathematically, a pronic number can be expressed as:
For example, the first few pronic numbers are:
𝑃 = 𝑛 ∗ (𝑛 + 1) 𝑛
𝑃1 = 0 * (0 + 1) = 0
𝑃2 = 1 ∗ (1 + 1) = 2
𝑃3 = 2 ∗ (2 + 1) = 6
𝑃4 = 3 ∗ (3 + 1) = 12

Example:
Input: n=20
Output: True
Explanation: 4 ∗ (4 + 1) = 20
'''

def is_pronic(n):
    for i in range(int(n**0.5)+1):
        if i*(i+1)==n:
            return True
    return False        
    

n=int(input())
print(is_pronic(n))
