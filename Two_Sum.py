#printing indices of the two numbers such that they add up to target.

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

