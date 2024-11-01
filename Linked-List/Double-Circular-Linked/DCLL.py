class Node(object):#1
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next



class DCLL(object):#2
    def __init__(self):
        self.start=None

    def empty(self):#3
        return self.start == None

    def insert_at_first(self,item):#4 
        if self.start is None:
            NewNode=Node(item=item)
            self.start=NewNode
            self.start.next=NewNode
            self.start.prev=NewNode
        else:
            NewNode=Node(item=item)
            NewNode.prev=self.start.prev
            NewNode.next=self.start
            self.start.prev.next=NewNode
            self.start.prev=NewNode
            self.start=NewNode


    def insert_at_last(self,item):#5 
        if self.start is not None:
            NewNode=Node(item=item)
            NewNode.prev=self.start.prev
            NewNode.next=self.start
            self.start.prev.next=NewNode
            self.start.prev=NewNode


    def search(self,key):#6
        temp=self.start
        while(True):
            if temp.item == key:
                print('Key Found')
                return temp
            temp=temp.next
            if temp == self.start:
                break
        print('Key Not Found ')
        return None

    
    def insert_after(self,key,item):#7 
        node=self.search(key)
        if node is not None:
            NewNode=Node(item=item)
            NewNode.prev=node
            NewNode.next=node.next
            node.next.prev=NewNode
            node.next=NewNode
        else:
            print(f"Key {key} not found. Cannot insert after it.")

    def print_list(self):#8
        if self.start is None:
            print(f"None-->")
            return
        temp=self.start
        while(True):
            print(f"{temp.item}-->",end=' ')
            temp=temp.next
            if temp == self.start:
                break
        print('Circular')
          
    def delete_first(self):#10 
        self.start.next.prev=self.start.prev
        self.start.prev.next=self.start.next
        self.start=self.start.next

    def delete_last(self):#11 
        if not self.empty():
            self.start.prev.prev.next=self.start
            self.start.prev=self.start.prev.prev

    def delete_item(self, dele): #12 
        if not self.empty():
            if self.start.item == dele:
                self.delete_first()
            else:
                temp=self.start
                while(temp.next != self.start):
                    if temp.next.item == dele:
                        temp.next.next.prev=temp
                        temp.next=temp.next.next
                        print(f"Item {dele} Deleted")
                        return
                    temp=temp.next
                print(f"Item {dele} not found.")
        
    def __iter__(self):
        if self.start is None:
            return DCLL_ITERATOR(None)
        else:
            return DCLL_ITERATOR(self.start)
            

class DCLL_ITERATOR:
    def __init__(self,start):
        self.current=start
        self.fast=start
        self.count=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.fast and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data

            

if __name__=="__main__":
    x=DCLL()
    x.insert_at_first(10)
    x.insert_at_first(20)
    x.insert_at_first(30)
    x.insert_at_last(5)
    x.insert_at_last(4)
    # x.insert_after(4,25)
    # x.delete_first()
    # x.delete_last()
    x.delete_item(30)
    x.print_list()

for i in (x):
    print(i,end=" ")