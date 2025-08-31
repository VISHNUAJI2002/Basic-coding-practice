"""
Find all the triplets in a list such that its sum equal to a particular 
target value (without printing duplicate triplets).

Example: 
input: nums = [5,3,2,1,-1,0,4] target = 5
output: [[0, 2, 3], [0, 1, 4], [-1, 1, 5], [-1, 2, 4]]
Notice that the order of the output and the order of the triplets does not matter.
"""


def threesum(nums,target):
    n=len(nums)
    nums.sort()
    res=set()

    for i in range(n):
        l=i+1
        r=n-1
        while l<r:
            summ=nums[i]+nums[l]+nums[r]
            if summ ==target:
                res.add((nums[i],nums[l],nums[r]))
                l+=1
                r-=1
            elif summ >target:
                r-=1
            else:
                l+=1
    res = [list(triplet) for triplet in res]
    return res

nums=list(map(int,input().split()))
target=int(input())
print(threesum(nums,target))
