#Fnd the longest common prefix string amongst an array of strings.

def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix=strs[0]
    for i in strs[1:]:
        while i[:len(prefix)]!=prefix:
            prefix=prefix[:-1]
            if not prefix:
                return ""
    return prefix        



s=input().split()
print(longestCommonPrefix(s))
    
