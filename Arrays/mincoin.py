'''
Given an infinite supply of each denomination of Indian currency {1,2,5,10,20,50,100,200,500,2000}
and a target value N.
Find the minimum number of coins and/or notes needed to make the change for Rs N.
Return the list containing the value of coins required. 
'''

def minPartition(x):
    currency = [2000,500,200,100,50,20,10,5,2,1]
    res = []
    for c in currency:
        while x >= c:
            x -= c
            res.append(c)
    return res


N=int(input())
print(minPartition(N))
