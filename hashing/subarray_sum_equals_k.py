"""
Problem Title: Subarray Sum Equals K
Description:
Given an array of integers nums and an integer k,
return the total number of continuous subarrays
whose sum equals to k.

Example 1:
Input:
nums = [1, 1, 1]
k = 2

Output:
2

Explanation:
Subarrays:
[1,1] (index 0-1)
[1,1] (index 1-2)


Example 2:
Input:
nums = [1, 2, 3]
k = 3

Output:
2

Explanation:
Subarrays:
[1,2]
[3]

Algorithm Explanation (Optimal - Prefix Sum + Hashing):
We use prefix sum and a hashmap.
Key Idea:
If current_sum - k exists in hashmap,
then a subarray with sum k exists.

Steps:
1. Initialize hashmap with {0:1}
2. Traverse array and maintain prefix sum
3. For each sum:
   - Check if (current_sum - k) exists
   - Add its frequency to result
4. Update hashmap with current_sum

Time Complexity:
O(n)
Space Complexity:
O(n)
"""


def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    hashmap = {0: 1}

    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in hashmap:
            count += hashmap[prefix_sum - k]
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
    return count


# Input/Output Section
nums = list(map(int, input().split()))
k = int(input())

print(subarray_sum(nums, k))
