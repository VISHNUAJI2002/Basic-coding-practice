'''
Solid square star pattern.

Example:
Input:
4
Output:
****
****
****
****
'''

def solid_square(n):
    for i in range(n):
        print('*' * n)

n = int(input())
solid_square(n)
