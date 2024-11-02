class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next


class Queue:
    def __init__(self):
        self.start=None
        self.end=None
        self.index_item=0

    def is_empty(self):
        return self.start == None

    def enqueue(self,item):
        NewNode=Node(item)
        if self.start is None:
            self.start=NewNode
            self.end=NewNode
        else:
            self.end.next=NewNode#Mast Concept yaha per ha [H]-->[10] ye jo  10 ha ye start v ha end v ha abb muje iske baad 20 add akrna ha kese karu self.end.next=newnode okk ab 10-->[20] lakin end pata kese chale ga iskliye hame self.end=NewNode kardena ha bas thats it
            self.end=NewNode
        self.index_item += 1


    def dequeue(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            if self.start is None:
                self.start=None
                self.end=None

            self.index_item-=1
            return data
        
        else:
            raise IndexError("Queue Under OverLap")
        
    def get_front(self):
        if not self.is_empty():
            return self.start.item
        
        else:
            raise IndexError("Queue Under OverLap")
    
    def get_rear(self):
        if not self.is_empty():
            return self.end.item
        else:
            raise IndexError("Queue Under OverLap")
        
    def size(self):
        return self.index_item
    

if __name__=="__main__":
    x=Queue()
    x.enqueue(10)
    # x.enqueue(20)
    # x.enqueue(30)
    # x.enqueue(40)
    try:
        print(f'Delete Element: {x.dequeue()}')
        print(f"Front Element: {x.get_front()}")
        print(f"Rear Element: {x.get_rear()}")
        print(f"Total Element: {x.size()}")
    except IndexError as e:
        print(e.args[0])

    
    
        