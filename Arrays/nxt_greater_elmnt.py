'''
find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, 
next greater of the last element is always -1.

Example:
Input: 5 3 1 2 4 6 0 8 9
Output: [6, 4, 2, 4, 6, 8, 8, 9, -1]
'''

def next_greater_elements(arr):
    n = len(arr)
    res = [-1] * n  #default result
    stack = []  #store indices
    
    for i in range(n-1,-1,-1): 
        while stack and arr[stack[-1]]<=arr[i]:
            stack.pop()
        if stack:
            res[i]=arr[stack[-1]]
        stack.append(i)
    return res

arr = list(map(int, input().split()))
print(next_greater_elements(arr))
