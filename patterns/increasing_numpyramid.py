#Increasing Numbers Pyramid

def increasing_numpyramid(n):
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        for j in range(1, i+1):
            print(j, end=" ")
        print()
        
n=int(input())
increasing_numpyramid(n)
