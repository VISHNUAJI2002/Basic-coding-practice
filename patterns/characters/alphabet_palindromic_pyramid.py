'''
Alphabet Palindromic Pyramid Pattern.
Given a number n, print a pyramid pattern where each row forms a palindrome using alphabets.

Example:
Input:
n = 5
Output:
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A

Explanation:
- Each row i (1 ≤ i ≤ n) first prints letters from 'A' to the i-th letter,
  then reverses them (excluding the last to avoid duplication).
- Spaces are added to center-align the pyramid.
'''

def alphabet_palindromic_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print("  " * (n - i), end="")

        # Ascending part (A → ...)
        for j in range(i):
            print(chr(65 + j), end=" ")

        # Descending part (... → A)
        for j in range(i - 2, -1, -1):
            print(chr(65 + j), end=" ")

        print() 


n = int(input())
alphabet_palindromic_pyramid(n)
