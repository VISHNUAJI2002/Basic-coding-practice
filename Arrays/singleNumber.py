'''
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.
You must implement a solution with a linear runtime 
complexity and use only constant extra space.

Example:
Input: nums = [2,2,1]
Output: 1
'''

def singleNumber(nums):
    res=0
    for i in nums:
        res=res^i
    return res    
    
    
nums=list(map(int,input().split()))
print(singleNumber(nums))
