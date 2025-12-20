'''
Largest Rectangle in Histogram.
Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
'''

def largest_rect_area(heights):
    n=len(heights)
    maxarea=0
    for i in range(n):
        minheight=heights[i]
        for j in range(i,n):
            minheight=min(minheight,heights[j])
            area=minheight*(j-i+1)
            maxarea=max(area,maxarea)
    return maxarea
    
heights=list(map(int,input().split()))
print(largest_rect_area(heights))
        
