'''
Given a number n, check whether it is a prime number or not.
A prime number is a number greater than 1 that has no divisors other than 1 and itself.

Example:
Input: 29
Output: True
'''

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input())
print(is_prime(n))
