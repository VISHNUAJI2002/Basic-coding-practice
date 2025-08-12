#return the length of the last word in the string.

def lengthOfLastWord(s):

    length=0
    s=s.strip()
    for i in range(len(s)-1,-1,-1):
        if s[i]==" ":
            break 
        else:
            length+=1
    return length


s=input()
print(lengthOfLastWord(s))
