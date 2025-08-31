'''
There are N hotels along the beautiful Adriatic coast. Each hotel has its value in Euros.
Sroljo has won M Euros on the lottery. Now he wants to buy a sequence of consecutive hotels,
such that the sum of the values of these consecutive hotels is as great as possible 
but not greater than M.
calculate this greatest possible total value.
Example:
Input:
5 12
2 1 3 4 5
Output:
12
'''

n,m=map(int,input().split())
h=list(map(int,input().split()))

j=0
summ=0
maxx=0
for i in range(n):
    summ+=h[i]
    while summ>m:
        summ-=h[j]
        j+=1
    if maxx<summ:
        maxx=summ
print(maxx) 
