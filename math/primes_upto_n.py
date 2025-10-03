'''
Print all prime numbers up to a number n.

Example:
Input: 10
Output: 2 3 5 7
'''

def primes(n):
    for i in range(2,n+1):
        is_prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            print(i,end=" ")
            
            
#using for-else: The else block executes only if the loop completes without a break.
def for_else(n):
    for i in range(2, n+1):
        for j in range(2, int(i**0.5) + 1):   
            if i % j == 0:
                break                         
        else:
            print(i, end=" ")                # else runs only if no break → prime            
            
    
n=int(input())
primes(n)
print()

for_else(n)
