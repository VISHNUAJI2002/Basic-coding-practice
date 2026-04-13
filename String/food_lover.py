"""
Problem Title: Food Lover

Description:
Rex bought food items represented by characters '1', '2', and '3'.
He can repeatedly perform the following operations until only one item remains:

1. Pick two different types of food items and convert them
   into a single item of the third type.

2. Pick two items of the same type and convert them
   into a single item of the same type.

Find the number of distinct possible food types
that can remain at the end.

Example:
Input:
121

Output:
2

Explanation:
Based on the reduction rules and character count parity,
there can be 2 distinct possible final food items.
"""


def food_lover(s):

    n = len(s)

    if n == 1:
        return 1

    if n == 2:
        return 1

    c1 = s.count('1')
    c2 = s.count('2')
    c3 = s.count('3')

    distinct = (c1 > 0) + (c2 > 0) + (c3 > 0)

    # Only one type present
    if distinct == 1:
        return 1

    # All counts have same parity
    if c1 % 2 == c2 % 2 == c3 % 2:
        return distinct

    # Different parity case
    return 3 if distinct == 3 else 2


# Input/Output Section
s = input().strip()
print(food_lover(s))
