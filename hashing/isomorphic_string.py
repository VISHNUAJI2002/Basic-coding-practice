"""
Problem Title: Isomorphic Strings
Description:
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if characters in s can be replaced to get t.
Each character must map to exactly one character,
and no two characters may map to the same character.

Example 1:
Input:
egg
add

Output:
True

Explanation:
e -> a
g -> d

Example 2:
Input:
foo
bar

Output:
False

Explanation:
o cannot map to two different characters.
"""


# Optimal Python Solution

def isomorphic_strings(s, t):

    if len(s) != len(t):
        return False

    map_s_t = {}
    map_t_s = {}

    for i in range(len(s)):

        if s[i] in map_s_t and map_s_t[s[i]] != t[i]:
            return False

        if t[i] in map_t_s and map_t_s[t[i]] != s[i]:
            return False

        map_s_t[s[i]] = t[i]
        map_t_s[t[i]] = s[i]

    return True


# User Input
s = input().strip()
t = input().strip()

print(isomorphic_strings(s, t))
