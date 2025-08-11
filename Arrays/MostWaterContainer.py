#container with most water
'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.'''

def area(h):
    maxarea=0
    l,r=0,len(h)-1
    while l<r:
        area=(min(h[l],h[r])*(r-l))
        maxarea=max(area,maxarea)
        if h[l]<h[r]:
            l+=1
        else:
            r-=1
    return maxarea        
    
heights=list(map(int,input().split()))
print(area(heights))
