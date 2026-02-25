"""
Problem Title: Maximum Subarray Sum
Description:
Given an integer array nums, find the contiguous subarray
which has the largest sum and return that sum.

Example:
Input:
-2 1 -3 4 -1 2 1 -5 4

Output:
6

Explanation:
The subarray [4, -1, 2, 1] has the largest sum = 6.
"""


def maximum_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# User Input
nums = list(map(int, input().split()))
print(maximum_subarray(nums))
