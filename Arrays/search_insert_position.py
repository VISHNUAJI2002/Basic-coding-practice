'''
Search Insert Position.
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
'''

def searchInsert(nums,target):
    l,r = 0, len(nums) - 1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return l  # position where target should be inserted

nums=list(map(int,input().split()))
target=int(input())
print(searchInsert(nums,target))

