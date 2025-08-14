'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

def validparentheses_stack(s):
    stack=[]
    for i in s:
        if i=='(':
            stack.append(')')
        elif i=='[':
            stack.append(']')
        elif i=='{':
            stack.append('}')
        else:    
            if not stack or stack[-1]!=i:
                return False
            else:
                stack.pop()
    if not stack:
        return True
    return False    
       
    
s=input()
print(validparentheses_stack(s))
