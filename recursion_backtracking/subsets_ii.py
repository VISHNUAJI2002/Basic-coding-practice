"""
Problem Title: Subsets II
Description:
Given an integer array nums that may contain duplicates,
return all possible subsets (the power set).
The solution set must not contain duplicate subsets.

Example 1:

Input:
nums = [1,2,2]
Output:
[
[],
[1],
[1,2],
[1,2,2],
[2],
[2,2]
]

Example 2:

Input:
nums = [0]
Output:
[
[],
[0]
]

Algorithm Explanation (Backtracking + Duplicate Skipping):
Steps:
1. Sort the array so duplicates become adjacent
2. Generate subsets using backtracking
3. At each level:
   - If current element equals previous element
   - Skip it to avoid duplicate subsets
4. Add every valid subset to result

Time Complexity:
O(2^n)
Space Complexity:
O(n)
"""


def subsets_with_dup(nums):
    nums.sort()
    result = []

    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result

# Input/Output Section
nums = list(map(int, input().split()))
for subset in subsets_with_dup(nums):
    print(subset)
