"""
Problem Title: Valid Anagram

Description:
Given two strings s and t, return True if t is an anagram of s,
otherwise return False.
An anagram is formed by rearranging the letters of one string
to produce the other string, using all characters exactly once.

Example 1:
Input:
s = "anagram"
t = "nagaram"

Output:
True

Explanation:
Both strings contain the same characters with the same frequency.

Example 2:
Input:
s = "rat"
t = "car"

Output:
False
"""


def is_anagram(s, t):

    if len(s) != len(t):
        return False

    frequency = {}

    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    for char in t:
        if char not in frequency:
            return False
        frequency[char] -= 1
        if frequency[char] < 0:
            return False
    return True




# Input/Output Section

s = input().strip()
t = input().strip()

print(is_anagram(s,t))
