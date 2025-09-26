'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example :
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
'''

def insert(intervals,new):
    merged=[]
    i=0
    n=len(intervals)
    while i<n and intervals[i][1]<new[0]:
        merged.append(intervals[i])
        i+=1
    while i<n and intervals[i][0]<=new[1]:
        new[0]=min(intervals[i][0],new[0])
        new[1]=max(intervals[i][1],new[1])
        i+=1
    merged.append(new)
    while i<n:
        merged.append(intervals[i])
        i+=1
    return merged    
    
    
no_of_intervals=int(input())
intervals=[list(map(int,input().split()))for _ in range(no_of_intervals)]
new_interval=list(map(int,input().split()))
print(insert(intervals,new_interval))

