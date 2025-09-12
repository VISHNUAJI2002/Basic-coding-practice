'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

def groupanagrams(strs):
    group={}
    for i in strs:
        key=''.join(sorted(i))              
        if key in group:                   # if key not in group:
            group[key].append(i)           #    group[key] = []                                                 
        else:                              # group[key].append(word)
            group[key]=[]
            group[key].append(i)
    return list(group.values())
    
strs=input().split()
print(groupanagrams(strs))
