"""
Problem Title: Prefix Word Pattern

Description:
Given a word, print a pattern where each line contains
an increasing prefix of the word starting from the first character.

Example:
Input:
hello

Output:
h
he
hel
hell
hello

Explanation:
The pattern is formed by printing prefixes of the word.
On each line, one more character is added from left to right.
"""

def print_prefix_pattern(word):
    for i in range(1, len(word) + 1):
        print(word[:i])

word = input().strip()
print_prefix_pattern(word)
