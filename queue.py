
#implemet queue using list
class Queue:
    
    def __init__(self,size):
        self.size=size
        self._store=list()
        
    def q_insert(self,element):
        if len(self._store)==self.size:
            raise "Queue out of bound"
        else:
            self._store.append(element)
    
    
    def dqueue(self):
        return self._store.pop(0)
    
    def q_peek(self):
        return self._store[0]
    

q1=Queue(2)
q1.q_insert(1)
q1.q_insert(2)
q1.q_insert(3)
print("Peeking first element",q1.q_peek())
q1.dqueue()
print("After deleting 1st element next element in queue is",q1.q_peek())
        
    