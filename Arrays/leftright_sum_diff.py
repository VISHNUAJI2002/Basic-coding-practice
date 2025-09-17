'''
You are given an integer array nums and an index k.
The left sum is defined as the sum of all elements strictly before index k.
The right sum is defined as the sum of all elements strictly after index k.
Your task is to return the absolute difference between the left sum and the right sum.

Example:
Input: nums = [2, 3, 5, 7, 11], k = 2  
Output: 13  
Explanation:  
Left sum = 2 + 3 = 5  
Right sum = 7 + 11 = 18  
Absolute difference = |5 - 18| = 13  
'''

def difference_by_k(nums,k):
    leftsum,rightsum=0,0
    n=len(nums)

    for i in range(n):
        if i<k:         
            leftsum+=nums[i]
        elif i>k:       
            rightsum+=nums[i]
    return abs(leftsum-rightsum)


nums = list(map(int,input().split()))
k = int(input())
print(difference_by_k(nums, k))

