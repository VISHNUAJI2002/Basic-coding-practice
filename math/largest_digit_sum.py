'''
Given an array of integers, for each element find the largest digit in that number.
Return the sum of these largest digits.

Example:
Input : 7,10,32
Output : 7+1+3 = 11
'''


def sum_of_largest_digits(nums):
    summ=0
    for i in nums:
        largest=0
        for j in str(i):
            largest=max(largest,int(j))
        summ+=largest
    return summ   
    
    
def one_liner(nums):
    return sum(max(int(dig)for dig in str(i)) for i in nums)
            

nums=list(map(int,input().split()))
print(sum_of_largest_digits(nums))
print(one_liner(nums))
