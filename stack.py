
#program to implement stack

class Stack:  
    
    def __init__(self,size):
        self.size=size
        self._store=list()
        
    def stack_push(self,element):
        self._store.append(element)
        
        
    def stack_pop(self):
        if len(self._store) == 0:
            raise ValueError("Stack is empty..")
        return self._store.pop(-1)
    
    def stack_peek(self):
        if len(self._store) == 0:
            raise ValueError("Stack is empty..")
        return self._store[-1]
    
    
    
stack1=Stack(4)
stack1.stack_push(2)   #adding elements in stack using stack_push method
print("peeking", stack1.stack_peek()) #checking top most element in stack
stack1.stack_push(3)
print("peeking", stack1.stack_peek())
stack1.stack_push(4)
print("peeking", stack1.stack_peek())
stack1.stack_push(1)
print("peeking", stack1.stack_peek())
print("popping",stack1.stack_pop())
print("popping",stack1.stack_pop())
print("peeking", stack1.stack_peek())
print("popping",stack1.stack_pop())
print("peeking", stack1.stack_peek())
print("popping",stack1.stack_pop())
print("peeking", stack1.stack_peek())



