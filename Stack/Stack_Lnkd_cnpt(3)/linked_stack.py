class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next


class Stack:
    def __init__(self):
        self.start=None
        self.item_count=0


    def is_empty(self):
        return self.item_count == 0
    

    def push(self,item):
        if self.start is None:
            self.start=item
            self.item_count += 1
        else:
            NewNode=Node(item)
            NewNode.next=self.start
            self.start=NewNode
            self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_count -= 1
            return data
    def peak(self):
        return self.start.item

    def size(self):
        return self.item_count

if __name__ == '__main__':
    x=Stack()
    x.push(10)
    x.push(20)
    x.push(30)
    x.push(40)
    print(f"Total Element: {x.size()}")
    print(f"Top Element: {x.peak()}")
    print(f"Delete Element: {x.pop()}")
    print(f"Delete Element: {x.pop()}")
    print(f"Top Element: {x.peak()}")
    print(f"Total Element: {x.size()}")