#creating linked list
from html.entities import name2codepoint


class Node:
    
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n1.next=n2
n2.next=n3
n3.next=n4

def print_linkedlist():
    t=n1
    while t!=None:
        print(t.val)
        t=t.next
        
print_linkedlist()

def add_node(n1,pos):
    t=n1
    while t==pos-1:
        print
        
        
        