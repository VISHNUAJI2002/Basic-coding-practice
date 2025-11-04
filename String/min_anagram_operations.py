'''
Anagram Operation Counter.
Given a string of even length consisting of digits or letters, 
find the minimum number of character changes required to make 
its first half an anagram of its second half.
An operation consists of changing one character in the first half.

Example 1:
Input:
s = "123123"
Output:
0
Explanation:
Both halves are already anagrams ("123" and "123").

Examole 2:
Input:
s = "111222"
Output:
3
Explanation:
All three characters in the first half need to change to match the second half ("111" → "222").
'''

def min_anagram_operations(s):
    n=len(s)
    mid=n//2
    first_half=s[:mid]
    second_half=s[mid:]
    
    freq_map={}
    operations=0
    
    for i in second_half:
        freq_map[i]=freq_map.get(i,0)+1
    
    for i in first_half:
        if i in freq_map and freq_map[i]>0:
            freq_map[i]-=1
        else:
            operations+=1
    return operations
    
    
s=input()
print(min_anagram_operations(s))  

