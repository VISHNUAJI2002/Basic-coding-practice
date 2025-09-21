'''
Diamond Shape Alphabet Pattern

Example:
Input:
4
Output:
   A 
  A B 
 A B C 
A B C D 
 A B C 
  A B 
   A 
   
'''


def diamond(n):
    for i in range(n):                  #Upper part
        print(" "*(n-i-1), end="")
        for j in range(i+1):
            print(chr(65+j), end=" ")
        print()
        
    for i in range(n-2,-1,-1):          #Lower part
        print(" "*(n-i-1), end="")
        for j in range(i+1):
            print(chr(65+j), end=" ")
        print()

n=int(input())
diamond(n)
