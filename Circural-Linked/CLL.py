class Node(object):#1
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next



class CLL(object):#2
    def __init__(self):
        self.tail=None

    
    def empty_ck(self):#3
        return self.tail == None
    
    def insert_at_first(self,item):#4
        NewNode=Node(item)
        if self.tail is None:
            self.tail=NewNode
            self.tail.next=NewNode
        else:
            NewNode.next=self.tail.next
            self.tail.next=NewNode

    def insert_at_last(self,item):#5
        NewNode=Node(item)
        if self.tail is None:
            self.tail=NewNode
            self.tail.next=NewNode
        else:
            NewNode.next=self.tail.next
            self.tail.next=NewNode
            self.tail=NewNode
    
    def search(self,key):#6
        temp=self.tail.next
        while(temp):
            if temp.item == key:
                print(f'Key {temp.item} Founded')
                return temp
            temp=temp.next
            if temp == self.tail.next:
                break
        print(f'Key {key} Not Found')
        return
        

    def insert_at_after(self,key,item):#7
        node=self.search(key)
        if node is not None:
            NewNode=Node(item,node.next)
            node.next=NewNode
            if node == self.tail:
                self.tail=NewNode
        # if self.tail is None:
        #     return
        # temp=self.tail.next
        # while(temp):
        #     if temp.item == node:
        #         NewNode=Node(item)
        #         NewNode.next=temp.next
        #         temp.next=NewNode
        #     temp=temp.next
        #     if temp == self.tail.next:
        #         break
    def print_func(self):#8
        temp=self.tail.next
        while(temp):
            print(f"{temp.item}-->",end=" ")
            temp=temp.next
            if temp == self.tail.next:
                break
        print('Circular')


    def delete_at_first(self):#10
        if self.tail is None:
            return
        self.tail.next=self.tail.next.next

    def delete_at_last(self):#11
        if self.tail is not None:
            if self.tail.next == self.tail:#ye Node ke liye ha ye
                self.tail=None
            else:
                temp=self.tail.next# ye pahle wala Node ha yaha se looping start hoga ex:1-->2-->3...
                while(temp.next != self.tail):
                    temp=temp.next
                self.tail=temp.next
                temp.next=self.tail.next
                
        
    def delete_item(self,node):#12
        if not self.empty_ck():
            if self.tail.next == node:# ager 1 he node ha to ye 
                self.tail=None
            else:
                if self.tail.next.item == node:
                    self.delete_at_first()
                else:
                    temp=self.tail.next
                    while(temp!=self.tail):
                        if self.tail.item == node:
                            self.delete_at_last()
                            break
                        if temp.next.item== node:
                            temp.next=temp.next.next
                            break
                        temp=temp.next
    
    def __iter__(self):#9
        if self.tail is None:
            return CLL_ITERATOR(None)
        else:
            return CLL_ITERATOR(self.tail.next)
                    

class CLL_ITERATOR:
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
    x=CLL()
    x.insert_at_first(10)
    x.insert_at_first(20)
    x.insert_at_first(30)
    x.insert_at_first(40)
    x.insert_at_last(4)
    x.insert_at_last(3)
    # x.delete_item(20)
    # x.insert_at_after(40,29)
    # x.search(1000)
    # x.delete_at_first()
    x.delete_at_last()
    # x.delete_item(10)
    x.print_func()
    for z in (x):
        print(z,end=",")