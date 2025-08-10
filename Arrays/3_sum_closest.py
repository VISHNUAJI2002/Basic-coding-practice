'''Find three integers in a list such that the sum is closest to target, and return the sum''' 

def three_sum_closest(nums, target):
    n=len(nums)
    nums.sort()
    closest_sum=nums[0]+nums[1]+nums[2]

    for i in range(n-2):
        l,r=i+1,n-1
        while l<r:
            current_sum=nums[i]+nums[l]+nums[r]
            if abs(current_sum-target)<abs(closest_sum-target):
                closest_sum=current_sum
            if current_sum<target:
                l+=1
            elif current_sum>target:
                r-=1
            else:
                return current_sum
                
    return closest_sum


nums=list(map(int,input().split()))
target=int(input())
print(three_sum_closest(nums,target))
