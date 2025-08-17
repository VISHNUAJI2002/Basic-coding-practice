#finding longest substring without duplicate characters and its length.

def solution(s):
    length=0
    current=""
    longest=""
    for i in s:
        if i in current:
            current=current[current.index(i)+1:]
        current+=i
        if len(current)>length:
            length=len(current)
            longest=current
    return(longest,length)
    
    
str=input()
print(solution(str))
