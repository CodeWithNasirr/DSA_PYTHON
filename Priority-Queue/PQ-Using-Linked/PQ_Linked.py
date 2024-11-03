class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next



class priority:
    def __init__(self):
        self.start=None
        self.index_item=0

    def push(self,item,priority):
        NewNode=Node(item,priority)
        if not self.start or priority<self.start.priority:
            NewNode.next=self.start
            self.start=NewNode
            self.index_item+=1

    def pop(self):
        if self.start is None:
            raise IndexError('Priority is Empty ')
        data=self.start.item
        self.start=self.start.next
        self.index_item-=1
        return data
    def size(self):
        return self.index_item
    
    def is_empty(self):
        return self.start == None


if __name__=="__main__":
    x=priority()
    x.push('Nasir',10)
    x.push("Asir",5)
    x.push('Xero',4)
    x.push('Zero',3)
    x.push('Hero',2)

    print(f'Total Element: {x.size()}')
    # print(f"Element Deleted: {x.pop()}")
    while not x.is_empty():
        print(x.pop())
    
        
