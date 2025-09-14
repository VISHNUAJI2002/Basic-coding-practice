'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs at the indices 0 and 3.

Approaches:
1. Hashing (Optimal) - O(n)
2. Sorting - O(n log n)
3. Brute Force - O(n²)
'''

def containsduplicate(nums):        #O(n)
    seen=set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)    
    return False
    

def sorting_method(nums):           #O(n log n)       
    nums.sort()
    n=len(nums)
    for i in range(1,n):
        if nums[i]==nums[i-1]:
            return True
    return False
    
    
def bruteforce(nums):               #O(n²)
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]==nums[j]:
                return True
    return False


nums = list(map(int,input().split()))
print("Optimal (Hashing):", containsduplicate(nums))
print("Sorting:", sorting_method(nums))
print("Brute Force:", bruteforce(nums))
