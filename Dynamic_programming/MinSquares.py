'''
Given a positive integer N, find the minimum number of perfect square numbers
(such as 1, 4, 9, 16, ...) whose sum is equal to N.
'''

def MinSquares(N):
    dp = [float('inf')]* (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        j = 1
        while j*j <= i:
            dp[i] = min(dp[i], dp[i- j*j]+1)
            j+=1
    return dp[N]


N = int(input())
print(MinSquares(N))

