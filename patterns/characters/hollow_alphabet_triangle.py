'''
Hollow Alphabet Triangle.
Given a number N, print a hollow triangle pattern using alphabets.
The pattern starts from 'A' at the top and continues alphabetically down to the base.

Example:
Input:
5
Output:
    A
   B B
  C   C
 D     D
EEEEEEEEE
'''

def hollow_alphabet_triangle(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        ch = chr(65 + i)
        if i == 0:
            print(ch)
        elif i == n - 1:
            print(ch * (2 * i + 1))
        else:
            print(ch + " " * (2 * i - 1) + ch)


n = int(input())
hollow_alphabet_triangle(n)
