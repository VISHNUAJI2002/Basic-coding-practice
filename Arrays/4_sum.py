'''
Find an array of all the unique quadruplets such that they add upto given target value:
nums[a] + nums[b] + nums[c] + nums[d] == target
a, b, c, and d are distinct.

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
    

nums=list(map(int,input().split()))
target=int(input())

print(foursum(nums,target))
