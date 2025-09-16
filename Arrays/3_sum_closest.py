'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
Example:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
''' 

def three_sum_closest(nums, target):
    n=len(nums)
    nums.sort()
    closest_sum=nums[0]+nums[1]+nums[2]

    for i in range(n-2):
        l,r=i+1,n-1
        while l<r:
            current_sum=nums[i]+nums[l]+nums[r]
            if abs(current_sum-target)<abs(closest_sum-target):
                closest_sum=current_sum
            if current_sum<target:
                l+=1
            elif current_sum>target:
                r-=1
            else:
                return current_sum              #current_sum==target
                
    return closest_sum


nums=list(map(int,input().split()))
target=int(input())
print(three_sum_closest(nums,target))

