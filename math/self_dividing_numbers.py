"""
Problem Title: Self Dividing Numbers
Description:
A self-dividing number is a number that is divisible
by every digit it contains.

A self-dividing number:
1. Cannot contain the digit 0
2. Must be divisible by each of its digits

Given two integers left and right,
return a list of all self-dividing numbers
in the range [left, right].

Example:

Input:
left = 1
right = 22

Output:
[1,2,3,4,5,6,7,8,9,11,12,15,22]

Explanation:
12 is self-dividing because:
12 % 1 = 0
12 % 2 = 0

15 is self-dividing because:
15 % 1 = 0
15 % 5 = 0

13 is NOT self-dividing because:
13 % 3 != 0

Algorithm Explanation:
For each number:
1. Extract each digit
2. If digit is 0 → invalid
3. If number is not divisible by digit → invalid
4. Otherwise it is self-dividing

Time Complexity:
O(n × d)

n = number of integers in range
d = number of digits

Space Complexity:
O(1)
"""

def is_self_dividing(num):
    original = num
    while num > 0:
        digit = num % 10
        if digit == 0:
            return False
        if original % digit != 0:
            return False
        num //= 10
    return True

def self_dividing_numbers(left, right):
    result = []
    for num in range(left, right + 1):
        if is_self_dividing(num):
            result.append(num)
    return result  

# Input/Output Section
left = int(input("Enter left value: "))
right = int(input("Enter right value: "))

print("Self-dividing numbers:")
print(self_dividing_numbers(left, right))
