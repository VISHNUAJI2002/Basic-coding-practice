'''
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

def long(nums):
    longest=0
    numset=set(nums)
    for i in numset:
        if i-1 not in numset:
            length=1
            while i+length in numset:
                length+=1
            longest=max(longest,length)
    return longest
    
    
nums=list(map(int,input().split()))
print(long(nums))
