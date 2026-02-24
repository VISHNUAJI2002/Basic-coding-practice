"""
Problem Title: House Robber

Description:
You are given an array where each element represents the amount of money
in a house. You cannot rob two adjacent houses.
Return the maximum amount of money you can rob without alerting the police.

Example:
Input:
2 7 9 3 1

Output:
12

Explanation:
Rob house 1 (2), house 3 (9), and house 5 (1).
Total = 2 + 9 + 1 = 12.
"""


def house_robber(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]


# User Input
nums = list(map(int, input().split()))
print(house_robber(nums))
