'''
Find all duplicate words in a given sentence.
Given a string sentence, return a sorted list of words that appear more than once. 
Words are considered case-sensitive (e.g., "Hello" and "hello" are different).

Example :
Input: "this is a test this is only a test"
Output: ['a', 'is', 'test', 'this']
Explanation: Words "this", "is", "a", and "test" appear more than once.
'''

def duplicates(s):
    s=s.split()
    seen=set()
    res=set()
    for i in s:
        if i in seen:
            res.add(i)
        else:  
            seen.add(i)
    return sorted(res)    

string=input()
print(duplicates(string))
