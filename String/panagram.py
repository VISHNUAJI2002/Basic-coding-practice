'''
check the given string is a "Panagram" or not. Return true if the string is a Panagram,
else return false.
A "Panagram" is a sentence containing every letter in the 
English Alphabet either in lowercase or Uppercase.
'''

def panagram(s):
    s=set([i.lower() for i in s if i.isalpha()])
    return len(s)==26

s=input()
print(panagram(s))
