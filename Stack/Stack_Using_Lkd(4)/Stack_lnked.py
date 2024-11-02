from SLL import *
class Stack:
    def __init__(self):
        self.sll=SingleLinked()
        self.index_item=0

    def is_empty(self):
        return self.sll.Check_Em
 

    def push(self,item):
        self.sll.insert_at_fast(item)
        self.index_item+=1

    def pop(self):
        if not self.is_empty():
            self.index_item-=1
            return self.sll.delete_first()

    def peek(self):
        if not self.is_empty():
            return self.sll.head.item
        else:
            raise IndexError("The Stack is Empty")
    
    def size(self):
        return self.index_item



if __name__=="__main__":
    x=Stack()
    # x.push(10)
    # x.push(20)
    # x.push(30)
    # x.push(40)
    print(f"Total Element: {x.size()}")
    x.pop()
    # print(f"Top Element: {x.peek()}")
    print(f"Total Element: {x.size()}")
