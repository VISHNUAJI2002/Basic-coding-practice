"""
Problem Title: Missing Number
Description:
Given an array nums containing n distinct numbers
in the range [0, n], return the only number
missing from the array.

Example 1:

Input:
nums = [3,0,1]
Output:
2
Explanation:
Numbers should be:
0,1,2,3
Missing number is 2.

Example 2:

Input:
nums = [0,1]
Output:
2

Example 3:

Input:
nums = [9,6,4,2,3,5,7,0,1]
Output:
8
"""


def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# Input/Output Section
nums = list(map(int, input().split()))
print(missing_number(nums))
