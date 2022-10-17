from ast import While


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

def print_linkedlist(start_node):
    temp_node=start_node
    while temp_node!=None:
        print(temp_node.val)
        temp_node=temp_node.next
        
# def print_list():
#     temp_node=node1
#     counter=1
#     while counter<pos:
#         print(temp_node.val) # a b
#         temp_node=temp_node.next # b c
#         counter+=1 # 2, 3
#     asf = temp_node.next 


def insert_node(newnode,pos):
    temp=node1
    counter=1
    while counter<pos:
        temp=temp.next
        counter+=1
    
    t=temp.next
    temp.next=newnode
    newnode.next=t
        

print("old list",print_linkedlist(node1))

newnode=Node('e')       
insert_node(newnode,2)
print("new list",print_linkedlist(node1)  ) 
