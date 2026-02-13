"""
Problem Title: Alphabet X Pattern

Description:
Given a word of odd length, print an 'X' pattern using its characters.

The first and last characters form the outer arms of the X,
and the middle character appears at the center.

Example:
Input:
HELLO

Output:
H   O
 E L
  L
 E L
H   O

Explanation:
Characters are printed diagonally from both ends towards the center,
forming an 'X' shape.
"""

def alphabet_x_pattern(word):
    n = len(word)

    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print(word[j], end="")
            else:
                print(" ", end="")
        print()


word = input().strip()
alphabet_x_pattern(word)
