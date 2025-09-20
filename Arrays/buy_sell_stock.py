'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.\
If you cannot achieve any profit, return 0.

Example :
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''


def maxProfit(prices):                #brute force - O(n²)
    maxprofit=0
    n=len(prices)
    for i in range(n):
        buy=prices[i]
        for j in range(i+1,n):
            profit=prices[j]-prices[i]
            maxprofit=max(maxprofit,profit)
    return maxprofit


def maxprofit_optimal(prices):        #optimal - O(n)
    buy=float('inf')
    maxprofit=0
    for i in prices:
        buy=min(buy,i)
        maxprofit=max(maxprofit,i-buy)
    return maxprofit


prices=list(map(int,input().split()))
print(maxProfit_optimal(prices))
