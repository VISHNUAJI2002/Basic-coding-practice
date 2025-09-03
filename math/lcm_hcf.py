'''
LCM & HCF of two numbers.
Example: 
Input:
8 12
Output:
LCM: 24
HCF: 4
'''

def hcf(a,b):      # Euclidean algorithm
    while b:
        a,b=b,a%b
    return a

def lcm(a, b):
    return (a*b)//hcf(a,b)

a,b=map(int,input().split())

print("LCM:", lcm(a, b))
print("HCF:", hcf(a, b))
