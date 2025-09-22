'''
Given two integers a and b, find their Greatest Common Divisor (GCD).
The GCD of two numbers is the largest positive integer that divides both numbers without leaving a remainder.
Constraints:
You must implement it using the Euclidean Algorithm (efficient, O(log(min(a, b)))).

Example:
Input: a = 48, b = 18  
Output: 6  
Explanation: Divisors of 48 → {1,2,3,4,6,8,12,16,24,48}  
             Divisors of 18 → {1,2,3,6,9,18}  
             Largest common divisor = 6

'''

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
    
    
a,b=map(int,input().split())
print(gcd(a,b))
        
