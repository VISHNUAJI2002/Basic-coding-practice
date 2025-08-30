'''
Find an array of all the unique quadruplets such that they add upto given target value:
nums[a] + nums[b] + nums[c] + nums[d] == target
a, b, c, and d are distinct.

Example:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''

def foursum(nums,t):
    nums.sort()
    n=len(nums)
    res=[]
    for i in range(n-3):
        for j in range(i+1,n-2):
            l,r=j+1,n-1
            while l<r:
                total=nums[i]+nums[j]+nums[l]+nums[r]
                if total==t:
                    res.append([nums[i],nums[j],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif total<t:
                    l+=1
                else:
                    r-=1
    res=[tuple(i)for i in res]
    res=set(res)
    res=[list(i)for i in res]
    return res

def optimized_4sum(nums,t):
    n=len(nums)
    nums.sort()
    res=[]
    for i in range(n-3):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            l,r=j+1,n-1
            while l<r:
                total=nums[i]+nums[j]+nums[l]+nums[r]
                if total==t:
                    res.append([nums[i],nums[j],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r-1]==nums[r]:
                        r-=1
                    l+=1
                    r-=1
                elif total<t:
                    l+=1
                else:
                    r-=1
    return res
    

nums=list(map(int,input().split()))
target=int(input())

print(foursum(nums,target))
print(optimized_4sum(nums,target))

