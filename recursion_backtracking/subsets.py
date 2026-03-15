"""
Problem Title: Subsets (Power Set)

Description:
Given an integer array nums containing unique elements, return all possible subsets
(the power set).

The solution set must not contain duplicate subsets.
The subsets can be returned in any order.

Example 1:
Input:
nums = [1,2,3]

Output:
[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

Explanation:
Every element has two choices:
1. Include it in the subset
2. Exclude it

So for n elements there will be 2^n possible subsets.


Example 2:
Input:
nums = [0]

Output:
[[], [0]]
"""


def generate_subsets(nums):
    result = []
    subset = []

    def backtrack(start):
        
        result.append(subset.copy())        # Add current subset to result

        for i in range(start, len(nums)):
            subset.append(nums[i])          # Choose element

            backtrack(i + 1)                # Explore further

            subset.pop()                    # Undo choice (backtrack)

    backtrack(0)
    return result


# User Input 

nums = list(map(int, input().split()))

subsets = generate_subsets(nums)

print("All subsets:")
for s in subsets:
    print(s)
