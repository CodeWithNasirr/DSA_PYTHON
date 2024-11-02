from SLL import *
class Stack(SingleLinked):

    def __init__(self):
        super().__init__()
        self.index_item=0


    def is_empty(self):
        return super().Check_Em()
    
    def push(self,item):
        self.insert_at_fast(item)
        self.index_item+=1

    def pop(self):
        if not self.is_empty():
            data=self.head.item
            self.delete_first()
            self.index_item-=1
            return data
        
    def peek(self):
        if not self.is_empty():
            return self.head.item
    
    def size(self):
        if not self.is_empty():
            return self.index_item
    

if __name__=='__main__':
    x=Stack()
    x.push(10)
    x.push(20)
    x.push(30)
    print(f"Total Element: {x.size()}")
    print(f"Delete Item: {x.pop()}")
    print(f"Top Element: {x.peek()}")
    print(f"Total Element: {x.size()}")
