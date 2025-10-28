'''
Minimum Moves to Reach Origin.
You are initially at the origin (0, 0) on a 2D plane. 
You are given a string s consisting of characters 'L', 'R', 'U', and 'D', representing moves:
- 'L' → move left
- 'R' → move right
- 'U' → move up
- 'D' → move down
You can modify some characters in s (change one move to another) such that you end up back at the origin after performing all moves.
Find the minimum number of modifications required to achieve this. 
It is guaranteed that it is always possible to return to the origin by modifying the string.

Example 1:
Input: s = "LRUD"
Output: 0
Explanation: Already ends up at the origin (0, 0).

Example 2:
Input: s = "LLLU"
Output: 2
Explanation: Changing one 'L' to 'R' and 'U' to 'D' brings you back to the origin.
'''

def min_moves_to_origin(s):
    l, r, u, d = 0, 0, 0, 0
    
    for i in s:
        if i == "L":
            l += 1
        elif i == "R":
            r += 1
        elif i == "U":
            u += 1
        elif i == "D":
            d += 1
    return (abs(l - r) + abs(u - d)) // 2


s = input().strip()
print(min_moves_to_origin(s))
