'''
Given a string s, find the length of the longest substring without duplicate characters.

Example :
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

def solution(s):
    length=0
    current=""
    for i in s:
        if i in current:
            current=current[current.index(i)+1:]
        current+=i
        if len(current)>length:
            length=len(current)
    return length
    
    
str=input()
print(solution(str))
