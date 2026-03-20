"""
Problem Statement:

You are given gym subscription plans:

Duration    Cost
1 month     2000
3 months    5000
6 months    9000
9 months    12000
12 months   15000

You need to calculate the total cost based on the input number of months.
Rules:
- The input must be divisible by 3.
- Use plans in priority: 12 → 9 → 6 → 3.
- Always choose the largest possible plan first.
- If not divisible by 3 → print "Error".

Example:
Input: 15
Output: 20000
Explanation:
12 months → 15000
3 months  → 5000
Total     → 20000
"""


def gym_fee(n):
    if n % 3 != 0:
        return "Error"
      
    cost = 0
    plans = [
        (12, 15000),
        (9, 12000),
        (6, 9000),
        (3, 5000)
    ]

    for months, price in plans:
        count = n // months
        cost += count * price
        n %= months

    return cost


# Input
n = int(input())

# Output
print(gym_fee(n))
