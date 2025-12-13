"""
Problem Title: Currency to INR Conversion

Description:
Given a currency code and an amount, convert the given amount into Indian Rupees (INR)
using predefined conversion rates.

Example:
Input:
1
10
Output:
650
Explanation:
The currency code 1 represents USD.
10 × 65 = 650 INR.
"""

def currency_to_inr(code, amount):
    rates = {1: 65, 2: 96, 3: 67, 4: 74, 5: 11}
    return amount * rates[code]

code = int(input().strip())
amount = int(input().strip())
print(currency_to_inr(code, amount))
