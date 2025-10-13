'''
Find the first non-repeating character in a string.

Example:
Input: "swiss"
Output: "w"
Explanation: 's' repeats, 'w' appears only once and first.
'''

def first_non_repeating_char(s):
    freq={}
    for i in s:                    
        freq[i]=freq.get(i,0)+ 1      # Count frequency of each character
        
    for i in s:
        if freq[i] == 1:
            return i
    return None  


s=input()
print(first_non_repeating_char(s))
