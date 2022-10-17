from traceback import print_list


class Node:
    
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
        

node1=Node('a')
node2=Node('b')
node3=Node('c')
node4=Node('d')
node1.next=node2
node2.next=node3
node3.next=node4

def print_list(startnode):
    t=startnode
    while t!=None:
        print(t.val)
        t=t.next
        
#print_list()

def insert_node(newnode,pos):
    if pos!=1:
        t=node1
        current_pos=1
        while current_pos!=pos-1:
            t=t.next
            current_pos+=1
        temp=t.next
        t.next=newnode
        newnode.next=temp
    else:
        newnode.next=node1
    

    

newnode=Node(5)
insert_node(newnode,5)

print_list(node1)


def del_node(pos):
    t=node1
    current_pos=1
    while current_pos!=pos-1:
        t=t.next
        current_pos+=1
    t.next=(t.next).next
        
        
del_node(5)
print("node after deletion")
print_list(node1)
    

def len_linkedlist(startnode):
    t=node1
    counter=0
    while t!=None:
        t=t.next
        counter+=1
        
    return counter

print(len_linkedlist(node1))

