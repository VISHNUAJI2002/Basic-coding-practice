'''
You are given an integer array nums where each element represents your maximum jump length at that position.
Determine if you can reach the last index starting from the first index.
Example:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

def canJump(nums):
    n=len(nums)
    if n==1:
        return True
    goal=n-1 
    for i in range(n-2,-1,-1):
        if i+nums[i]>=goal:
            goal=i
    return goal==0
    

nums=list(map(int,input().split()))
print(canJump(nums))
