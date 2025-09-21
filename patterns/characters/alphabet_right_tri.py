'''
Right Triangle with Alphabets.
Example:
Input:
4
Output:
A 
B B 
C C C 
D D D D 
'''


def alphabet_right_tri(n):
    ch=65
    for i in range(n):
        for j in range(i+1):
            print(chr(ch),end=' ')
        ch+=1
        print()    
            
    
n=int(input())
alphabet_right_tri(n)
