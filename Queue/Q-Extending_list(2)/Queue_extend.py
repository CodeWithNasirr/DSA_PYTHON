class Queue(list):
    def is_empty(self):
        return len(self)==0
    
    def enqueue(self,item):
        self.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            data=self[0]
            self.pop(0)
            return data
        else:
            raise IndexError('Queue Overlap')
        
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError('Queue Overlap')
        

    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('Queue Overlap')
        
    def size(self):
        return len(self)
    


if __name__=="__main__":
    x=Queue()
    x.enqueue(10)
    x.enqueue(20)
    x.enqueue(30)
    x.enqueue(40)
    try:
        print(f"Delete Element: {x.dequeue()}")
        print(f"Front Element: {x.get_front()}")
        print(f"Rear Element: {x.get_rear()}")
        print(f"Total Element: {x.size()}")
    except IndexError as e:
        print(e.args[0])
