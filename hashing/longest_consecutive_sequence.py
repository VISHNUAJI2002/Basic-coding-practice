"""
Problem Title: Longest Consecutive Sequence

Description:
Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.
The algorithm must run in O(n) time.

Example:
Input:
nums = [100, 4, 200, 1, 3, 2]
Output:
4

Explanation:
The longest consecutive sequence is [1, 2, 3, 4].
Its length is 4.
"""


def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest

nums = list(map(int, input().split()))
print(longest_consecutive(nums))
