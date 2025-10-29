'''
Maximum Anagram Group Size.
Given a list of strings, find the maximum number of strings that are anagrams of each other.
Two strings are anagrams if one can be formed by rearranging the characters of the other.

Example:
Input:
s=[bat,tab,pat,tap,cat]
Output:
2
Explanation:
"bat" and "tab" are anagrams, "tap" and "pat" are anagrams.
The largest group of anagrams has size 2.
'''

def max_anagram(s):
    n=len(s)
    anagram_count={}
    for word in s:
        sorted_word=''.join(sorted(word))
        if sorted_word in anagram_count:
            anagram_count[sorted_word]+=1
        else:
            anagram_count[sorted_word]=1
          
    return max(anagram_count.values()) if anagram_count else 0
    
    
def using_get_function(s):
    n = len(s)
    anagram_count = {}
    for word in s:
        sorted_word = ''.join(sorted(word))
        anagram_count[sorted_word] = anagram_count.get(sorted_word, 0) + 1
    return max(anagram_count.values()) if anagram_count else 0    


s=list(input().split())
print(max_anagram(s))
print(using_get_function(s))

