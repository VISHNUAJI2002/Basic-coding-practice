'''
You are given a number. Check whether the number of odd divisors 
of this number is equal to the number of even divisors.
If the counts are equal return True, otherwise False.

example:
input:14
output:True
'''

def Equal_odd_even_divisors(n):
    odd=0
    even=0
    for i in range(1,n+1):
        if (n%i==0):
            if i%2==0:
                even+=1
            else:
                odd+=1
    if (odd==even):
        return True
    else:
        return False
        
n=int(input())
print(Equal_odd_even_divisors(n))
