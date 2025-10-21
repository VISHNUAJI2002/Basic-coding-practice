'''
Plus One.
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
             Incrementing by one gives 123 + 1 = 124.
             Thus, the result should be [1,2,4].
'''


def plus_one(digits):       #Optimal
    n=len(digits)
    for i in range(n-1,-1,-1):
        if digits[i]<9:
            digits[i]+=1
            return digits
        digits[i] = 0       #carry over
    return [1] + [0] * n    # If all digits were 9, add 1 at the front


def plusOne(digits):
    n=len(digits)
    string=str(digits[0])
    for i in range(1,n):
        string+=str(digits[i]) 
    num=str(int(string)+1)
    l=[int(k) for k in num] 
    return l


digits_1 = list(map(int, input().split()))
print(plus_one(digits_1))
digits_2 = list(map(int, input().split()))
print(plusOne(digits_2))
