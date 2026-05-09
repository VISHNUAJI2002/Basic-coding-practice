"""
Problem Title: Largest Rectangle in Histogram
Description:
Given an array heights representing the heights of histogram bars,
return the area of the largest rectangle in the histogram.
Each bar has width = 1.

Example 1:
Input:
heights = [2,1,5,6,2,3]

Output:
10

Explanation:
The largest rectangle is formed using bars [5,6]
Width = 2
Height = 5
Area = 5 × 2 = 10

Example 2:
Input:
heights = [2,4]

Output:
4

Algorithm Explanation (Optimal - Monotonic Stack):
Key Idea:
For every bar, find:
1. First smaller bar on left
2. First smaller bar on right

The bar can expand between them.
We use a stack that stores indices of bars
in increasing height order.
Whenever we encounter a smaller height:
- taller bars cannot continue further
- so we calculate their maximum possible area

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


def largest_rectangle_area(heights):

    stack = []
    max_area = 0
    heights.append(0)
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            area = height * width
            max_area = max(max_area, area)
        stack.append(i)
    return max_area


# Input/Output Section
heights = list(map(int, input().split()))
print(largest_rectangle_area(heights))
