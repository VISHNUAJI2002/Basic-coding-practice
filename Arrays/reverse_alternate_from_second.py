'''
Given an array. Select the alternative elements in the array starting from second position.
Reverse these elements and place them in the array

Example:
Input : 1 5 6 7 8 9 0
Output : 1 9 6 7 8 5 0
'''


def rev_alternate_from_second(nums):
    n=len(nums)
    alternate=nums[1::2][::-1]
    j=0
    for i in range(1,n,2):
        nums[i]=alternate[j]
        j+=1
    return nums    

nums=list(map(int,input().split()))
print(rev_alternate_from_second(nums))
