# Queue implementaion using List
q = []
while True:
    print("0 - Exit")
    print("1 - Print Front & Rear")
    print("2 - Enqueue")
    print("3 - Dequeue")
    print("4 - Size")
    print("5 - Clear")
    n = int(input())
    if n==0:
        break
    elif n==1:
        if q:
            print("Front =",q[0])
            print("Rear =",q[-1])
        else:
            print("Queue is Empty")
    elif n==2:
        val = int(input())
        q.append(val)
        print(f'Inserted {val} at rear')
    elif n==3:
        if q:
            print(f'Deleted {q.pop(0)} from front')
        else:
            print("Empty Queue,deletion not possible")
    elif n==4:
        print("Size =",len(q))
    elif n==5:
        q.clear()
        
        
        
        
        
