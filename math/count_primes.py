"""
Problem Title: Count Primes
Description:
Given an integer n, return the number of prime numbers that are strictly less than n.
A prime number is a number greater than 1 that has no positive divisors
other than 1 and itself.

Example 1:
Input:
n = 10
Output:
4

Explanation:
The prime numbers less than 10 are:
2, 3, 5, 7
So the count is 4.

Example 2:
Input:
n = 0
Output:
0

Algorithm Explanation (Sieve of Eratosthenes):

Instead of checking each number individually for primality,
we use the Sieve of Eratosthenes to eliminate non-prime numbers.

Steps:
1. Create a boolean list where each index represents whether the number is prime.
2. Initially assume every number is prime.
3. Mark 0 and 1 as not prime.
4. Start from 2 and go up to sqrt(n).
5. If a number is prime, mark all of its multiples as not prime.
6. Start marking from i*i because smaller multiples were already handled.
7. After the sieve process, count the remaining True values.

Optimization Used:
We use Python slicing to mark multiples efficiently.

Example:
If i = 3, we mark
9, 12, 15, 18 ...

This is done with:
is_prime[i*i : n : i]

Time Complexity:
O(n log log n)

Space Complexity:
O(n)
"""


def count_primes(n):
    if n < 3:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            start = i * i
            is_prime[start:n:i] = [False] * len(range(start, n, i))   #Mark multiples of i as non-prime

    count = 0   #Count remaining primes
    for value in is_prime:
        if value:
            count += 1
    return count

# User Input 
n = int(input())
result = count_primes(n)
print(result)
