'''
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise. 
That means if a permutation of s1 exists as a substring of s2, then return true.
Both strings only contain lowercase letters.

Example :
Input: s1 = "abc", s2 = "lecabee"
Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".
'''

def checkInclusion(s1,s2):
    s1=sorted(s1)
    n=len(s2)
    for i in range(n-1):
        for j in range(i+1,n):
            substr=sorted(s2[i:j+1])
            if s1==substr:
                return True
    return False
    
    
s1=input()
s2=input()
print(checkInclusion(s1,s2))
