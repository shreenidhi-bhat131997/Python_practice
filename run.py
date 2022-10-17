class Node:
    
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

        
root=Node(1)
child1=Node(2)
child2=Node(3)
child3=Node(4)
child4=Node(5)
child5=Node(6)

root.left=child1
root.right=child2
child1.left=child3
child1.right=child4
child2.right=child5




def pre_order(root):
    if root==None:
        return
    else:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)
        

pre_order(root)
        
        
def post_order()