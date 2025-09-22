'''
Armstrong Number Check.
Given an integer n, determine whether it is an Armstrong number (also known as a narcissistic number).
A number is considered an Armstrong number if the sum of its digits, each raised to the power of the number of digits, is equal to the number itself.

Example :
Input: 153  
Output: True  
Explanation: 1³ + 5³ + 3³ = 153
'''

def armstrong(x):
    power=len(str(x))
    summ=0
    for i in str(x):
        summ=summ+int(i)**power
    if summ==x:
        return True
    return False
    
x=int(input())
print(armstrong(x))
        
