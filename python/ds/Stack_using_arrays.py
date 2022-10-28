import sys
from array import *
a=array('i',[])
while True:
    print("1.push 2.pop 3.display 4.exit")
    ch=int(input())
    if ch==1:
        ele=int(input())
        a.append(ele)
        print("Inserted")
    elif ch==2:
        if len(a)==0:
            print("Stack is empty")
        else:
            print("Deleted element is : ",a.pop())
    elif ch==3:
        if len(a)==0:
            print("Stack is empty")
        else:
            print("the elements in the stack are:")
            for i in a:
                print(i)
    elif ch==4:
        sys.exit()
    else:
        print("Invalid choice")