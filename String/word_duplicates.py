#Find all duplicate words in a given sentence.

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
