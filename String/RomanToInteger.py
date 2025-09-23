'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example :
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
'''

def RomanToInt(s):
    roman={'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    total=0
    n=len(s)
    for i in range(n):
        if i<n-1 and roman[s[i]]<roman[s[i+1]]:
            total-=roman[s[i]]
        else:
            total+=roman[s[i]]
    return total

def RomanToInt_2(s):
    roman={'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    total=0
    prev=0
    for i in reversed(s):
        if roman[i]<prev:
            total-=roman[i]
        else:
            total+=roman[i]
        prev=roman[i]
    return total 
    
    
s=input()
print(RomanToInt(s))
print(RomanToInt_2(s))
