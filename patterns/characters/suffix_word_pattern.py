"""
Problem Title: Suffix Word Pattern
Description:
Given a word, print a pattern where each line contains
an increasing suffix of the word starting from the last character.

Example:
Input:
hello

Output:
o
lo
llo
ello
hello

Explanation:
The pattern is formed by printing suffixes of the word.
On each line, one more character is added from the left.
"""

def print_suffix_pattern(word):
    n = len(word)
    for i in range(n - 1, -1, -1):
        print(word[i:])


word = input().strip()
print_suffix_pattern(word)
