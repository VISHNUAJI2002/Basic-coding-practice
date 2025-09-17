'''
Number triangle (right angled)

Example:
Input:
5
Output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

def num_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
        
n=int(input())
num_triangle(n)
