'''
Return first Repeated Character
Example:
Input: greater
Output: e
'''

def firstrep(s):
    seen=set()
    for i in s:
        if i in seen:
            return i
        seen.add(i)
    return None    

s=input()
print(firstrep(s))
