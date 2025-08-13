#kth largest element in a list

def kthlargest(arr,k):
    arr=list(set(arr))
    arr.sort()
    if len(arr)<k:
        return None
    return arr[-k]
    
    
nums=list(map(int,input().split()))
k=int(input())
print(kthlargest(nums,k))


    
