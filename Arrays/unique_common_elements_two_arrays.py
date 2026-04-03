"""
Problem Title: Unique Common Elements from Two Arrays

Description:
Given two arrays, find all unique common elements present in both arrays.

The output should contain each common element only once.

Example:
Input:
Array 1: [1, 2, 3, 4, 5]
Array 2: [3, 4, 4, 5, 6, 7]

Output:
[3, 4, 5]

Explanation:
The elements 3, 4, and 5 are present in both arrays.
Even though 4 appears multiple times in the second array,
it is included only once in the output.
"""


def find_unique_common_elements(arr1, arr2):

    set1 = set(arr1)
    set2 = set(arr2)
    result = list(set1 & set2)
    return result


# Input/Output Section

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

common = find_unique_common_elements(arr1, arr2)

print(common)
