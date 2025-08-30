'''
Find indices of the two numbers in an array such that they add up to target.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

def firstmethod(arr,t):
    n=len(arr)
    res=[]
    for i in range(n-1):
        for j in range(i,n):
            if arr[i]+arr[j]==t:
                res.append([i,j])
    return res            

def secondmethod(arr,t):
    mydict={}
    res=[]
    i=0
    for j in arr:
        diff=t-j
        if diff in mydict:
            res.append([mydict[diff],i])
        mydict[j]=i
        i+=1
    return res    



nums = list(map(int, input().split()))
target = int(input())

#first method
print(firstmethod(nums,target))
#second method
print(secondmethod(nums,target))
