"""
Problem Title: Merge Sorted Array
Description:
You are given two sorted arrays nums1 and nums2.
nums1 has a size of m + n where:
- First m elements are valid
- Last n elements are placeholders (0)
Merge nums2 into nums1 so that nums1 becomes
one sorted array.

Example 1:

Input:
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Output:
[1,2,2,3,5,6]

Example 2:

Input:
nums1 = [1]
m = 1
nums2 = []
n = 0
Output:
[1]

Example 3:

Input:
nums1 = [0]
m = 0
nums2 = [1]
n = 1
Output:
[1]

Algorithm Explanation (Optimal - Three Pointers):

We merge from the end of nums1.
Pointers:
i -> last valid element in nums1
j -> last element in nums2
k -> last position in nums1

Steps:
1. Compare nums1[i] and nums2[j]
2. Place larger element at nums1[k]
3. Move corresponding pointer
4. Continue until nums2 is exhausted

Time Complexity:
O(m + n)
Space Complexity:
O(1)
"""


def merge_sorted_array(nums1, m, nums2, n):

    i = m - 1
    j = n - 1
    k = m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1


# Input/Output Section
nums1 = list(map(int, input().split()))
m = int(input())

nums2 = list(map(int, input().split()))
n = int(input())

result = merge_sorted_array(nums1, m, nums2, n)
print(result)
