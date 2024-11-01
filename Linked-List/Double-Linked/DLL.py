class Node(object):#1
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next


class DLL(object):#2
    def __init__(self):
        self.head=None

    def CheckEmp(self):#3
        return self.head == None

    def insert_at_start(self,item):#4
        if self.head is None:
            NewNode=Node(None,item)
            self.head=NewNode
        else:
            NewNode=Node(None,item,self.head)
            self.head.prev=NewNode
            self.head=NewNode

    def insert_at_last(self,item):#5
        # NewNode=Node(item=item)#Mehod 1
        # if self.head is None:
        #     self.head=NewNode
        #     return
        # temp=self.head
        # NewNode=Node(temp.next.prev,item)
        # while(temp.next is not None):
        #     temp=temp.next
        # temp.next=NewNode
        NewNode=Node(item=item)#Method 2
        if self.head is None:
            self.head=NewNode
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=NewNode
        NewNode.prev=temp
        
    
    def search(self,key):#6
        temp=self.head
        while(temp):
            if temp.item == key:
                print(f"Key {temp.item}Founded ")
                return temp
            temp=temp.next
            if temp == self.head:
                break
        print(f"kEY {key} Not Founded")
        return
    
    def insert_after(self,node,item):#7
        if node is not None:
            NewNode=Node(node,item,node.next)
            if node.next:
                node.next.prev=NewNode
            node.next=NewNode

    
            
    def print_func(self):#8
        temp=self.head
        while(temp):
            print(f"{temp.item}-->",end=" ")
            temp=temp.next
        print('None')
    

    def __iter__(self):
        return DLLITERABLE(self.head)



    
    def delete_first(self):#10
        if self.head is None:
            return
        else:
            self.head=self.head.next
    def delete_last(self):#11
        if self.head is None:
            return
        elif self.head.next is None:
            self.head=None
        temp=self.head
        while(temp.next.next is not None):
            temp=temp.next
        temp.next=None
    
    def delete_item(self,dele):#12
        if self.head is None:#ager head pe kuch nhi ha to return kardo
            return
        elif self.head.next is None:#ager node bas 1 he ha or wo barabar horaha ha dele ke to usko None kardo else ayge bado
            self.head.item == dele
            self.head=None
        else:#ageer 1 se jyda node ha to temp=self.head means first Node if first node bara bar ha to uska head to usse barabar balee ke ayge set kardo or uska prev value head pe set kardo digram bana ke kar samaj jayega perfectly
            temp=self.head
            if temp.item == dele:
                self.head = temp.next
                temp.next.prev=self.head
                temp=temp.next
            while(temp.next is not None):
                if temp.next.item == dele:
                    temp.next=temp.next.next #iska matlan ye ha ager [prev|400|None]ye jo next.next ha ye None ko point karega and then last wala delete hojayega
                    break
                temp=temp.next

class DLLITERABLE:

    def __init__(self,start):
        self.current=start

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        
        data=self.current.item
        self.current=self.current.next
        return data


if __name__=="__main__":
    x=DLL()
    x.insert_at_start(10)
    x.insert_at_start(20)
    x.insert_at_start(30)
    x.insert_at_last(100)
    x.insert_at_last(200)
    x.insert_at_last(300)
    x.insert_at_last(400)
    # x.search(1000)
    # x.insert_after(x.search(100),50)
    # x.delete_first()
    # x.delete_last()
    x.delete_item(400)
    x.print_func()

for i in (x):
    print(i,end=" ")
