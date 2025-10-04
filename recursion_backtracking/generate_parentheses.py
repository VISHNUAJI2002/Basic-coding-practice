'''
Generate Parentheses.
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''

def generateParentheses(n):
    res=[]
    def backtrack(left,right,s):
        if len(s)==n*2:
            res.append(s)
            return
        if left<n:
            backtrack(left+1,right,s+'(')
        if right<left:
            backtrack(left,right+1,s+')')
    backtrack(0,0,'')
    return res


n=int(input())
print(generateParentheses(n))

