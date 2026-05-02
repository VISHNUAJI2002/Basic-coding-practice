"""
Problem Title: Maximum Product Subarray
Description:
Given an integer array nums, find a contiguous subarray
within the array which has the largest product,
and return that product.
A subarray is a continuous part of the array.

Example 1:
Input:
nums = [2, 3, -2, 4]
Output:
6

Explanation:
Subarray [2,3] gives product = 6

Example 2:
Input:
nums = [-2, 0, -1]
Output:
0

Explanation:
Subarray [-2, -1] is not contiguous (due to 0),
so maximum product is 0

Algorithm Explanation (Optimal - Dynamic Programming):
Key Idea:
At each position, we track:
1. max_product ending here
2. min_product ending here

Why min?
Because multiplying two negative numbers gives a positive number.

Steps:
1. Initialize:
   max_product = nums[0]
   min_product = nums[0]
   result = nums[0]
2. Traverse array from index 1:
   - If current number is negative → swap max and min
   - Update max_product = max(num, num * max_product)
   - Update min_product = min(num, num * min_product)
   - Update result
3. Return result

Time Complexity:
O(n)
Space Complexity:
O(1)
"""

def max_product_subarray(nums):
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        if num < 0:
            max_product, min_product = min_product, max_product
        max_product = max(num, num * max_product)
        min_product = min(num, num * min_product)
        result = max(result, max_product)
    return result

# Input/Output Section
nums = list(map(int, input().split()))
print(max_product_subarray(nums))
