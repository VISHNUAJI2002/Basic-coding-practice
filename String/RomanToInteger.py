#convert given roman numeral into an integer.

def RomanToInt(s):
    roman={'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    total=0
    n=len(s)
    for i in range(n):
        if i<n-1 and roman[s[i]]<roman[s[i+1]]:
            total-=roman[s[i]]
        else:
            total+=roman[s[i]]
    return total

def RomanToInt_2(s):
    roman={'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    total=0
    prev=0
    for i in reversed(s):
        if roman[i]<prev:
            total-=roman[i]
        else:
            total+=roman[i]
        prev=roman[i]
    return total 
    
    
s=input()
print(RomanToInt(s))
print(RomanToInt_2(s))
