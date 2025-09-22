'''
Given a string
If the string contain vowels replace every character of the string with first occurring vowel, 
If the string does not contain a vowel return original string

Example:
Input : BOB
Output : OOO

Explanation :
First occurring vowel in the string is O
So BOB ==> OOO
'''


def replace_with_fst_vowel(s):
    vowels=set('aeiouAEIOU')
    fst=None
    for i in s:
        if i in vowels:
            fst=i
            break
    if fst:    
        return fst*len(s)
    return s    
    
s=input()
print(replace_with_fst_vowel(s))
