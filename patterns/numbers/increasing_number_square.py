'''
Square pattern with increasing numbers in each row.

Example:
Input: 
4
Output:
1234
1234
1234
1234
'''


def increasing_number_square(n):
    for _ in range(n):
        for j in range(1, n+1):
            print(j, end="")
        print()

n = int(input())
increasing_number_square(n)
