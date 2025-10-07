'''
Decimal to Binary conversion.
Example:
Input: 10
Output: 1010
'''

def dec_to_bin(n):
    if n==0:
        return '0'
    negative=False
    if n<0:
        negative=True
        n=abs(n) 
    bits=[]
    while n>0:
        bits.append(str(n%2))
        n=n//2
    bits.reverse()
    binary=''.join(bits)
    if negative:
        return '-'+binary
    else:
        return binary


def dec_to_bin_function(n):
    if n >= 0:
        return bin(n)[2:]     # remove "0b" prefix
    else:
        return '-' + bin(n)[3:]    # remove "-0b" prefix
        

n=int(input())
print(dec_to_bin(n))
print(dec_to_bin_function(n))

