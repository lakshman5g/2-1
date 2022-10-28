class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
        print("haha")
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            print("hehe")
        else:
            n=self.head
            print("abc")
            while n.ref is not None:
                n=n.ref
                n.ref=new_node
                print("foff")
    def add_after(self,data,x):
        n=self.head
        print("sena")
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("node is present in linked list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
ll1=linkedlist()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.add_end(100)
ll1.add_after(20,40)
ll1.print_ll()

