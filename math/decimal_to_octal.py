'''
Decimal to Octal Conversion (Without Built-in Functions).
Given a decimal (base 10) number, convert it to its equivalent
octal (base 8) number manually.

Example:
Input:
n = 111
Output: 157
Explanation:
111 / 8 = 13 remainder 7
13 / 8 = 1 remainder 5
1 / 8 = 0 remainder 1
Reading remainders from bottom → 157
'''


def decimal_to_octal(n):
    if n == 0:
        return "0"
    octal_digits = []
    while n > 0:                 # Divide by 8 repeatedly
        remainder = n % 8
        octal_digits.append(str(remainder))
        n //= 8
    return ''.join(reversed(octal_digits))      # Reverse collected digits


n = int(input().strip())
print(decimal_to_octal(n))
