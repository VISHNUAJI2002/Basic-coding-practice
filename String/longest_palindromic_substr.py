'''
Given a string s, return the longest palindromic substring in s.
Example :
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
'''

def palindrome(s):
    if len(s)<=1:
        return s
    pal=""
    substr=""
    n=len(s)
    for i in range(n-1):
        for j in range(i,n):
            substr=s[i:j+1]
            if substr==substr[::-1]:
                if len(substr)>len(pal):
                    pal=substr
        if len(pal)>=n-i:
            return pal            
    return pal                
    
s=input()
print(palindrome(s))

