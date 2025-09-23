'''
Two numbers x and y are read by user
x = a + b
y = a — b
The output is value of z = a * b

Example:
Input : x = 7 , y = 1
Output : 12
Explanation :
x = 7 = 4 + 3
y = 1 = 4–3
So z = 4 * 3 = 12
'''

def product(x,y):
    a=(x+y)//2
    b=(x-y)//2
    return a*b
    
x=int(input())
y=int(input())
print(product(x,y))
