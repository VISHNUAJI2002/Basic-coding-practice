'''
Given a string
If the string contain palindrome of length 4 increase score value by 5
If the string contain palindrome of length 5 increase the score value by 10 Initially score is 0.

Example:
Input string : ABABAAAA
Output : 15
Explanation :
“ABABA”AAA palindrome of length 5 (now score = 10)
ABAB“AAAA” palindrome of length 4(now score = 10+5=15)
'''

def palindrome_score(s):
    n=len(s)
    score=0
    for i in range(n-3):
        if s[i:i+4]==s[i:i+4][::-1]:
            score+=5
    for i in range(n-4):
        if s[i:i+5]==s[i:i+5][::-1]:
            score+=10
    return score


s=input()
print(palindrome_score(s))
