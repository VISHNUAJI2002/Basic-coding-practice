'''
Given an array of intervals where intervals[i] = [startᵢ, endᵢ], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example :
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
'''


def merge(intervals):
    merged=[]
    intervals.sort()
    for i in intervals:
        if not merged or merged[-1][1]<i[0]:
            merged.append(i)
        else:
            merged[-1][1]=max(merged[-1][1],i[1])
    return merged
    

no_of_elements=int(input())
intervals=[list(map(int,input().split()))for _ in range(no_of_elements)]
print(merge(intervals))
