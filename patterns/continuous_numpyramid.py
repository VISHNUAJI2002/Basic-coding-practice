#Continuous Numbers Pyramid

def continuous_numpyramid(n):
    num = 1
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        for j in range(1, i+1):
            print(num, end=" ")
            num += 1
        print()
    
n=int(input())
continuous_numpyramid(n)
