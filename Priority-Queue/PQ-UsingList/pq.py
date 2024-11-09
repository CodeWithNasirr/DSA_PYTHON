class priority:
    def __init__(self):
        self.list=[]
     
    def push(self,item,priority):
        index=0
        while(index<len(self.list)) and self.list[index][1]<=priority:
            index+=1
        self.list.insert(index,(item,priority))
    
    def is_empty(self):
        return len(self.list)==0
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Priority is Empty ')
        data=self.list[0][0]
        self.list.pop(0)
        return data    

    def size(self):
        return len(self.list)
if __name__=="__main__":
    x=priority()
    x.push("Nasir",5)
    x.push("Alio",54)
    x.push("Balio",1)
    x.push("Liadi",4)
    # print(f'Total Element: {x.size()}')
    # print(f"Element Deleted: {x.pop()}")
    # print(f'Total Element: {x.size()}')
    while not x.is_empty():
        print(x.pop())
