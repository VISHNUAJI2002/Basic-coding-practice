'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

Example :
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''

def climbStairs(n):
    if n <= 2:
        return n   
    dp= [0]*(n+1)   # dp[i] will store number of ways to reach step i
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]   # recurrence relation
    return dp[n]


n=int(input())
print(climbStairs(n))
