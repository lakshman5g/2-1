import sys
from array import *
q=array('i',[])
def enquque():
    ele=int(input())
    q.append(ele)
    print("Added")
def dequque():
    if not q:
        print("Empty quque")
    else:
        e=q.pop()
        print("Removed element is",e)
def display():
    print("the elements in the quque are:")
    for i in q:
        print(i)
while True:
    print("1.add 2.remove 3.show 4.exit")
    ch=int(input())
    if ch==1:
        enquque()
    elif ch==2:
        dequque()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("Invalid choice")
