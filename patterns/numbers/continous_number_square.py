'''
Continuous number square pattern.

Example:
Input: 
4
Output:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''

def continuous_number_square(n):
    num=1
    for i in range(n):
        for j in range(n):
            print(num,end=" ")
            num+=1
        print()

n = int(input())
continuous_number_square(n)
