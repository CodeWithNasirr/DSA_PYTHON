from SLL import *

class Queue:
    def __init__(self):
        self.sll=SingleLinked()
        self.index_item=0

    def is_empty(self):
        return self.sll.Check_Em()
    
    def enqueue(self,item):
        self.sll.insert_at_fast(item)
        self.index_item+=1

    def dequeue(self):
        if not self.is_empty():
            data=self.sll.head.item
            self.sll.delete_first()
            self.index_item-=1
            return data

    def get_front(self):
        if not self.is_empty():
            return self.sll.head.item

    def get_rear(self):
        if not self.is_empty():
            return self.sll.end.item
        
    def size(self):
        return self.index_item
        
    

if __name__=="__main__":
    x=Queue()
    x.enqueue(10)
    x.enqueue(20)
    x.enqueue(30)
    x.enqueue(40)
    try:
        print(f'Delete Element: {x.dequeue()}')
        print(f"Front Element: {x.get_front()}")
        print(f"Rear Element: {x.get_rear()}")
        print(f"Total Element: {x.size()}")
    except IndexError as e:
        print(e.args[0])