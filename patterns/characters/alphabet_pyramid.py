'''
Right Triangle with Alphabets.
Example:
Input:
4
Output:
   A 
  A B 
 A B C 
A B C D 
'''


def continuous_alphabet_right_tri(n):
    for i in range(n):
        print(" "*(n-i-1),end="")
        for j in range(i+1):
            print(chr(65+j),end=" ")
        print()    
            
n=int(input())
continuous_alphabet_right_tri(n)
