'''
Number square pattern.

Example:
Input:
4
Output:
1111
2222
3333
4444
'''


def number_square(n):
    for i in range(1, n+1):
        print(str(i) * n)


n = int(input())
number_square(n)
