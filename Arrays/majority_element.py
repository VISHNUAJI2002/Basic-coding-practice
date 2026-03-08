"""
Problem Title: Majority Element
Description:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n/2⌋ times.
You may assume that the majority element always exists.

Example 1:

Input:
3 2 3
Output:
3

Example 2:

Input:
2 2 1 1 1 2 2
Output:
2
"""

# Approach 1: Hash Map
# Time: O(n)
# Space: O(n)


def majority_element_hashmap(nums):
    freq = {}
    n = len(nums)

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

        if freq[num] > n // 2:
            return num


# Approach 2: Boyer–Moore Voting Algorithm
# Time: O(n)
# Space: O(1)

def majority_element_boyer_moore(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate



# User Input

nums = list(map(int, input().split()))

print("HashMap Result:", majority_element_hashmap(nums))
print("Boyer-Moore Result:", majority_element_boyer_moore(nums))
