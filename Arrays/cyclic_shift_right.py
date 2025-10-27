"""
Cyclic Shift Right.
Given an array A of length N and an integer K, perform a cyclic (circular) right shift
on the array K times. That means each element moves right by one position per shift,
and the elements shifted out from the right reappear at the beginning.

Example:
Input: 
N = 5,A = [1, 2, 3, 4, 5],K=2
Output ('A' modified in place):
[4, 5, 1, 2, 3]
Explanation:
Right shifting by 2 means last two elements [4,5] move to the front.
"""

def cyclic_shift_right(N,A,K):
    if N == 0:
        return
    k_effective = K % N

    A[:] = A[-k_effective:] + A[:-k_effective]


N=int(input())
A=list(map(int,input().split()))
K=int(input())
cyclic_shift_right(N,A,K)
print(A)
