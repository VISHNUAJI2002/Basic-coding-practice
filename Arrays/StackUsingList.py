# Stack implementaion using list
stack = []
while True:
    print("0 - Exit")
    print("1 - Print top")
    print("2 - Push")
    print("3 - Pop")
    print("4 - Size")
    print("5 - Clear")
    n = int(input())
    if n==0:
        break
    elif n==1:
        if stack:
            print("Top =",stack[-1])
        else:
            print("Stack is Empty")
    elif n==2:
        val = int(input())
        stack.append(val)
        print(val,"pushed into stack")
    elif n==3:
        if stack:
            print(stack[-1],"poped from stack")
            stack.pop()
        else:
            print("Empty stack,deletion not possible")
    elif n==4:
        print("Size =",len(stack))
    elif n==5:
        stack.clear()
