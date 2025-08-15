# print uncommon characters between two strings lexicographily

def uncommonchars1(s1,s2):
    a = set(s1)
    b = set(s2)
    c = a.symmetric_difference(b)
    res = ""
    for i in sorted(c):
        res += i
    return res

    
s1=input()
s2=input()
print(uncommonchars1(s1,s2))
