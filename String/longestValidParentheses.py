'''
Given a string s containing just the characters '(' and ')', 
return the length of the longest valid (well-formed) parentheses substring.
A valid parentheses substring is one where every opening parenthesis '(' 
has a matching closing parenthesis ')' in the correct order.
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
