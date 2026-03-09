"""
Problem Title: Search a 2D Matrix

Description:
You are given an m x n matrix where:
1. Each row is sorted in non-decreasing order.
2. The first element of each row is greater than the last element of the previous row.
Return True if the target exists in the matrix, otherwise False.
Time Complexity Required: O(log(m*n))

Example:
Input:
3 4
1 3 5 7
10 11 16 20
23 30 34 60
target = 3

Output:
True
"""

# ------------------------
# Optimal Python Solution
# ------------------------

def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:

        mid = (left + right) // 2

        row = mid // cols
        col = mid % cols

        value = matrix[row][col]

        if value == target:
            return True

        elif value < target:
            left = mid + 1

        else:
            right = mid - 1

    return False


# -------------
# User Input
# -------------
r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
target = int(input())

print(search_matrix(matrix, target))
