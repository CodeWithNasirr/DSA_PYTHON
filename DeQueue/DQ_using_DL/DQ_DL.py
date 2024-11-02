class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next


class dequeue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.front == None
    
    def insert_front(self,item):
        NewNode=Node(item=item)
        if self.front is None:
            self.front=NewNode
            self.rear=NewNode
        else:
            NewNode.prev=self.front.prev
            NewNode.next=self.front
            self.front.prev=NewNode
            self.front=NewNode
        self.item_count+=1
    
    def insert_rear(self,item):
        NewNode=Node(item=item)
        if self.is_empty():
            self.rare=NewNode
        else:
            NewNode.prev=self.rear
            self.rear.next=NewNode
            self.rear=NewNode
        self.item_count+=1


    def delete_front(self):
        if not self.is_empty():
            data=self.front.item
            if self.front.next is None:
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next
            self.item_count-=1
            return data
        else:
            raise IndexError()
        
    
    def delete_rear(self):
        if not self.is_empty():
            data=self.rear.item
            if self.rear.prev is None:
                self.front=None
                self.rear=None
            else:
                self.rear=self.rear.prev
                self.rear.next=None
            self.item_count-=1
            return data
        else:
            raise IndexError()



    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Empty List")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Empty List")
    
    def size(self):
        return self.item_count

if __name__=="__main__":
    x=dequeue()
    x.insert_front(10)
    x.insert_front(20)
    x.insert_front(30)
    x.insert_rear(40)
    x.insert_rear(50)
    try:
        print(f"Top Element: {x.get_front()}")
        print(f"Last Element: {x.get_rear()}")
        print(f"Delete Front Element: {x.delete_front()}")
        print(f"Delete Rear Element: {x.delete_rear()}")
        print(f"Total Element: {x.size()}")
    except IndexError as e:
        print(f"Empty List {e.args}")




