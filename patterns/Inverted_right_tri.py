#Inverted right-angled triangle (stars)

def inverted_right_tri(n):
    for i in range(n,0,-1):
        print("*" * i)
        
        
n=int(input())
inverted_right_tri(n)
