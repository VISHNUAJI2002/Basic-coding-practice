'''
Check if Array is Monotonic.
An array is called monotonic if it is either entirely non-increasing or non-decreasing.

Example 1:
Input:
arr = [1, 2, 2, 3]
Output:
True
Explanation:
The array elements are in non-decreasing order.

Example 2:
Input:
arr = [6, 5, 4, 4]
Output:
True
Explanation:
The array elements are in non-increasing order.

Example 3:
Input:
arr = [1, 3, 2]
Output:
False
Explanation:
The array is neither non-increasing nor non-decreasing.
'''

def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing
  

arr = list(map(int, input().split()))
print(is_monotonic(arr))
