"""
Problem Title: Number Plus (+) Pattern
Description:
Given an odd number n, print a plus (+) pattern of size n × n
using numbers.
- The middle row is filled with numbers from 1 to n.
- The middle column is filled with numbers from 1 to n.
- All other positions are printed as spaces.

Example:
Input:
5

Output:
  1  
  2  
12345
  4  
  5  

Explanation:
For n = 5:
- Middle row index = 2
- Middle column index = 2
Numbers are printed along the central row and column,
forming a plus (+) shape.
"""


def number_plus_pattern(n):
    middle = n // 2

    for i in range(n):
        for j in range(n):
            if i == middle:
                print(j + 1, end="")
            elif j == middle:
                print(i + 1, end="")
            else:
                print(" ", end="")
        print()


n = int(input().strip())
number_plus_pattern(n)
