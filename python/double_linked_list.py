class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class doublell:
    def __init__(self):
        self.head=None
    def printll(self):
        if self.head is None:
            print("DLL is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end='')
                n=n.nref
    def printll_reverse(self):
        print()
        if self.head is None:
            print("Dll is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,'-->',end='')
                n=n.pref
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("ll is not empty")
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        print("in add_end")
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
                n.nref=new_node
                new_node.pref=n
dl=doublell()
dl.printll()
dl.printll_reverse()
dl.insert_empty(45)
dl.add_begin(37)
dl.add_end(32)
dl.printll()
dl.printll_reverse()
