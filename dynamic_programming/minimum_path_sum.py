"""
Problem Title: Minimum Path Sum

Description:
Given an m x n grid filled with non-negative numbers, find a path
from the top-left corner to the bottom-right corner that minimizes
the sum of all numbers along its path.

You can only move either RIGHT or DOWN at any point.

Example:
Input:
3 3
1 3 1
1 5 1
4 2 1

Output:
7

Explanation:
The path 1 → 3 → 1 → 1 → 1 gives the minimum sum = 7.
"""


def minimum_path_sum(grid):
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0]*cols for _ in range(rows)]

    dp[0][0] = grid[0][0]

    # first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # first column
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # rest of the grid
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[rows-1][cols-1]


# User Input
r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

print(minimum_path_sum(grid))
