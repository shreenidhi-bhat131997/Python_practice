class Node:
    #creating a linked list
    def __init__(self,val,next=None):  
        #val is for storing value and next variable is for storing address
        self.val=val
        self.next=next



n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)

n1.next=n2
n2.next=n3
n3.next=n4


#printing node elements
t=n1
while t!=None:
    print(t.val)
    t=t.next

    
 

