class Stack:
    
    def __init__(self):
        self._store=list()
        
    def stackpush(self,element):
        self._store.append(element)
        print(f'{element} has been added to stack')
        
    def stackpop(self):
        return self._store.pop()
    
    def stackpeek(self):
        return self._store[-1]
    
    
stack1=Stack()
stack1.stackpush(1)
stack1.stackpush(2)
print("topmost element is",stack1.stackpeek())
stack1.stackpush(3)
print("after adding topmost element is",stack1.stackpeek())
stack1.stackpop()
print("after deleting topmost element is",stack1.stackpeek())

