"""
Problem Title: Check if One String is Rotation of Another

Description:
Given two strings s and goal, return True if and only if
s can become goal after some number of shifts (rotations).
A shift means moving the first character of s to the end.

Example 1:
Input:
s = "abcde"
goal = "cdeab"

Output:
True

Explanation:
After shifting "abcde" → "bcdea" → "cdeab"


Example 2:
Input:
s = "abcde"
goal = "abced"

Output:
False

Explanation:
No rotation can form "abced"
"""


def is_rotation(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)


# Input/Output Section

s = input().strip()
goal = input().strip()

print(is_rotation(s, goal))
