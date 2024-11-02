class Queue:
    def __init__(self):
        self.list=[]


    def is_empty(self):
        return len(self.list) == 0
    
    def enqueue(self,item):
        self.list.append(item)

    def dequeue(self):
        if not self.is_empty():
            data=self.list[0]
            self.list.pop(0)
            return data
        else:
            raise IndexError('Queue UnderFlow')
    
    def get_front(self):
        if not self.is_empty():
            return self.list[0]
        else:
            raise IndexError('Queue UnderFlow')
    
        
    
    def get_rear(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            raise IndexError('Queue UnderFlow')
        
    
    def size(self):
        return len(self.list)
        

if __name__=="__main__":
    x=Queue()
    x.enqueue(10)
    x.enqueue(20)
    x.enqueue(30)
    x.enqueue(40)
    try:
        x.dequeue()
        print(f"Front Element: {x.get_front()}")
        print(f"Rear Element: {x.get_rear()}")
        print(f"Total Element: {x.size()}")
    except IndexError as e:
        print(e.args[0])
