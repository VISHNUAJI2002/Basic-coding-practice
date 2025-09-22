'''
kth largest element in a list.
Given an array of integers and an integer k, return the k-th largest unique element in the array.
If the array has fewer than k unique elements, return None.

Example:
Input: arr = [3, 1, 5, 2, 5, 3], k = 2  
Output: 3
Explanation:
Unique elements = [3, 1, 5, 2]  
Sorted = [1, 2, 3, 5]  
2nd largest = 3  
'''


def kthlargest(arr,k):
    arr=list(set(arr))
    arr.sort()
    if len(arr)<k:
        return None
    return arr[-k]
    
    
nums=list(map(int,input().split()))
k=int(input())
print(kthlargest(nums,k))


    
