'''
Longest Valid Parentheses.
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
'''

def longestValidParentheses(s):
    stack = [-1]  
    max_len = 0
    
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i) 
        else:
            stack.pop()       
            if not stack:
                stack.append(i) 
            else:
                max_len = max(max_len, i - stack[-1])
    
    return max_len
              

s = input().strip()
print(longestValidParentheses(s))
