'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]
'''

def productExceptSelf(nums):
    prod,zero_cnt=1,0
    n=len(nums)
    for num in nums:
        if num:
            prod *= num
        else:
            zero_cnt +=  1
    if zero_cnt > 1: 
        return [0]*n
    if zero_cnt==1:
        res=[0]*n
        res[nums.index(0)]=prod
        return res
    else:
        res=[prod//i for i in nums]
        return res    


nums=list(map(int,input().split()))
print(productExceptSelf(nums))
