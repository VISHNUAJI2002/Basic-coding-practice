'''
Binary to Decimal conversion.
Example:
Input: 1010
Output: 10
'''

def bin_to_decimal(binary):
    res,power=0,0
    for bit in reversed(binary):
        if bit=="1":
            res+=2**power
        power+=1
    return res


binary=input()
print(bin_to_decimal(binary))
