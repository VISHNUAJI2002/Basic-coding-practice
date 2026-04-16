"""
Problem Title: Isomorphic Strings
Description:
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if characters in s can be replaced
to get t while preserving order.
Each character must map to exactly one character,
and no two characters can map to the same character.

Example 1:
Input:
s = "egg"
t = "add"

Output:
True

Example 2:
Input:
s = "foo"
t = "bar"

Output:
False
"""


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    map_st = {}
    map_ts = {}
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        if char_s in map_st:
            if map_st[char_s] != char_t:
                return False
        else:
            map_st[char_s] = char_t
        if char_t in map_ts:
            if map_ts[char_t] != char_s:
                return False
        else:
            map_ts[char_t] = char_s
    return True

# Input/Output Section
s = input().strip()
t = input().strip()

print(is_isomorphic(s, t))
