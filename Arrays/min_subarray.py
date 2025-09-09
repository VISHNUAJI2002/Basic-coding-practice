'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example :

Input: nums = [3, -4, 2, -3, -1, 7, -5]
Output: -6
Explanation: The subarray [-4, 2, -3, -1] has the smallest sum -6.
'''

def minsubarray(nums):
    minn=float('inf')
    summ=0
    for i in nums:
        summ+=i
        minn=min(minn,summ)
        if summ>0:
            summ=0
    return minn
    
nums=list(map(int,input().split()))
print(minsubarray(nums))
