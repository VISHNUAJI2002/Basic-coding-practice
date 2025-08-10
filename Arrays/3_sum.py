"""printing all the triplets in a list such that its sum equal to a particular 
   target value (without printing duplicate triplets)."""

nums=list(map(int,input().split()))
target=int(input())

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
res=list(res)        
print(res)            
