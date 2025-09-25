'''
Quicksort algorithm.
example:
input: 3 1 5 0 2 6 4 7 9 8
output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''


def quick(arr,low,high):
    if low<high:
        j=partition(arr,low,high)
        quick(arr,low,j-1)
        quick(arr,j+1,high)
        
def partition(arr,low,high):
    i,j,pivot=low,high,low
    while i<j:
        while i<=high and arr[i]<=arr[pivot]:
            i+=1
        while j>=low and arr[j]>arr[pivot]:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[j],arr[pivot]=arr[pivot],arr[j]
    return j            
            
     
arr=list(map(int,input().split()))
quick(arr,0,len(arr)-1)
print(arr)
