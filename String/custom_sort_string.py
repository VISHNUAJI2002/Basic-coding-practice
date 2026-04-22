"""
Problem Title: Custom Sort String
Description:
You are given two strings:

1. order → represents a custom order of characters
2. s     → the string that needs to be rearranged

Your task is to rearrange the characters of string s such that:
- Characters follow the order defined in "order"
- If a character appears multiple times, include all its occurrences
- Characters not present in "order" can appear at the end in any order

Important:
This is NOT normal alphabetical sorting. The string "order" defines
a custom priority of characters.

Example 1:
Input:
order = "cba"
s = "abcd"

Output:
"cbad"

Explanation:
Priority from "order":
c → first
b → next
a → next

So we take characters from s in this order:
c → present → take it
b → present → take it
a → present → take it

Remaining character:
d (not in order) → added at the end
Final result: "cbad"

Example 2:
Input:
order = "kqep"
s = "pekeq"

Output:
"kqeep"

Explanation:
Count characters in s:
p → 1
e → 2
k → 1
q → 1

Now follow "order":
k → 1 time
q → 1 time
e → 2 times
p → 1 time
Final result: "kqeep"

Algorithm Explanation (Hashing + Controlled Traversal):
Steps:
1. Count frequency of each character in string s
2. Traverse the "order" string:
   - For each character, append it as many times as it appears in s
   - Remove it from the frequency map
3. Append remaining characters (not present in "order")

Time Complexity:
O(n + m)
Space Complexity:
O(n)
Where:
n = length of s
m = length of order
"""


def custom_sort_string(order, s):
    frequency = {}          # Count frequency of characters in s

    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    result = []

    for char in order:      # Add characters based on custom order
        if char in frequency:
            result.append(char * frequency[char])
            del frequency[char]

    for char in frequency:  # Add remaining characters
        result.append(char * frequency[char])

    return "".join(result)


# Input/Output Section
order = input().strip()
s = input().strip()

print(custom_sort_string(order, s))
