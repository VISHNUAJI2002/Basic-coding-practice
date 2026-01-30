"""
Problem Title: Reverse Alphabet Triangle
Description:
Given a number n, print a reverse alphabet triangle pattern
starting from 'A'.

Example:
Input:
5

Output:
ABCDE
ABCD
ABC
AB
A

Explanation:
The pattern starts with the first n alphabets.
On each next line, the last alphabet is removed,
forming a reverse triangular shape.
"""

def reverse_alphabet_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(chr(ord('A') + j), end="")
        print()


n = int(input().strip())
reverse_alphabet_triangle(n)
