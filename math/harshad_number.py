'''
Check if a number is a Harshad (Niven) number.
Example:
Input: 18
Output: True
Explanation: 1 + 8 = 9, and 18 is divisible by 9.
'''

def is_harshad(n):
    if n == 0:
        return False
    digit_sum = 0
    temp = abs(n)
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    return n % digit_sum == 0


n = int(input())
print(is_harshad(n))
