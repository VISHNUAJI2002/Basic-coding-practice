'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example :

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''

def maxsubarray(nums):
    maxx=float('-inf')
    summ=0
    for i in nums:
        summ+=i
        maxx=max(maxx,summ)
        if summ<0:
            summ=0
    return maxx
    
nums=list(map(int,input().split()))
print(maxsubarray(nums))
    
