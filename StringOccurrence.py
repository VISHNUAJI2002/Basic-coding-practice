'''For two strings main and sub, return the index of the 
first occurrence of sub in main, or -1 if sub is not part of main.
'''

def strstr(s1,s2):
    n=len(s1)
    m=len(s2)
    if n<m:
        return -1
    for i in range(n+1-m):
        if s1[i]==s2[0]:
            if s1[i:i+m]==s2:
                return i
    return -1            
main=input()
sub=input()
print(strstr(main,sub))
