'''
Check if a number is an Automorphic Number.
An Automorphic number is a number whose square ends with the same digits as the number itself.

Example:
Input: 76
Output: True
Explanation: 76² = 5776 → ends with 76
'''

#without using string operations
def is_automorphic(n):
    sq=n*n
    temp=abs(n)
    digits=0              # Find number of digits in n
    while temp>0:
        digits+=1
        temp//=10

    return sq%(10**digits)==abs(n)        


#using string operations
def automorphic(n):
    sq = n * n
    return str(sq).endswith(str(abs(n)))
    

n = int(input())
print(is_automorphic(n))
print(automorphic(n))


