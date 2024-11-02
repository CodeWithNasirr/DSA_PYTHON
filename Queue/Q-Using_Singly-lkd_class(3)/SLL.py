class Node(object):#Q1
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
 
 
class SingleLinked(object): #Q2
    def __init__(self,head=None):
        self.head=head
        self.end=None
        
    def Check_Em(self):#Q3
            return self.head==None


    def insert_at_fast(self,item):#Q4
        NewNode=Node(item)
        if self.head == None:
            self.head=NewNode
            self.end=NewNode
        else:
            self.end.next=NewNode
            self.end=NewNode
        
    def insert_at_last(self,item):#Q5
        NewNode=Node(item)
        temp=self.head
        if not temp == None:
            while(temp.next != None):
                temp=temp.next
            temp.next=NewNode
        else:
            self.head=NewNode
        

    def search(self,key):#Q6
        temp=self.head
        while(temp):
            if temp.item == key:
                print('Key Found')
                return temp
            temp=temp.next
        print('Key Not Found ')
        return None
        

    def insert_after(self,node,item):#Q7
        if node is not None:
            NewNode=Node(item,node.next)
            node.next=NewNode
            
    def printFunc(self):#Q8
        temp=self.head
        while(temp):
            print(f"{temp.item}-->",end=" ")
            temp=temp.next
        print('None')




    def __iter__(self):#Q9
        return SLLITERATOR(self.head)





    def delete_first(self):#Q10
        if self.head is not None:
            self.head=self.head.next

    def delete_last(self):#Q11
        if self.head is None:
            return
        elif self.head.next is None:#this is for only 1 node
            self.head=None
        else:
            temp=self.head
            while(temp.next.next is not None):
                temp=temp.next
            temp.next=None
    
    def delete_item(self,item):#Q12
        if self.head is None:# This Code is For list Empty Ho To Ye
            return
        elif self.head.next is  None:# This Code is For  Ager list pe bas 1 Node Ho 
            if self.head.item == item:
                self.head=None
            else:
                return
        else:
            temp=self.head # Ye Temp ka matalba ye ha ki ye wo self.head nhi ha ye uska reference ha maltaba [H]-->[N] ye to Node[N] ha
            if temp.item == item:#ager list pe multiple Node ho to ager fast Node pe delete_item()Rakhdeya jayega to ye uskeliye
                self.head=temp.next
            else:
                while (temp.next is not None):#
                    if temp.next.item == item:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
          
class SLLITERATOR:
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

