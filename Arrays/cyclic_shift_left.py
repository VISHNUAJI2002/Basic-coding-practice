'''
Cyclic Shift Left.
Given an array A of length N and an integer K, perform a cyclic (circular) left shift
on the array K times. That means each element moves left by one position per shift,
and the elements shifted out from the left reappear at the end.

Example:
Input:
N = 5
A = [1, 2, 3, 4, 5]
K = 2
Output:
[3, 4, 5, 1, 2]
Explanation:
After 1st shift → [2, 3, 4, 5, 1]
After 2nd shift → [3, 4, 5, 1, 2]
'''

def cyclic_shift_left(N,A,K):
    if N == 0:
        return []
    k_effective = K % N     # Effective shift (avoid unnecessary full rotations)
    A[:]= A[k_effective:] + A[:k_effective]


N=int(input())
A=list(map(int,input().split()))
K=int(input())
cyclic_shift_left(N,A,K)
print(A)

