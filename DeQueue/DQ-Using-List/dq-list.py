class Dequeue:
    def __init__(self):
        self.list=[]

    def is_empty(self):
        return len(self.list)==0

    def insert_front(self,item):
        self.list.insert(0,item)
    
    def insert_rear(self,item):
        self.list.append(item)

    def delete_front(self):
        if not self.is_empty():
            data=self.list[0]
            self.list.pop(0)
            return data
        else:
            raise IndexError("Empty List")
        
    
    def delete_rear(self):
        if not self.is_empty():
            data=self.list[-1]
            self.list.pop()
            return data
        else:
            raise IndexError("Empty List")
        
    def get_front(self):
        if not self.is_empty():
            return self.list[0]
        else:
            raise IndexError("Empty List")
    

    def get_rare(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            raise IndexError("Empty List")
        
    
    def size(self):
        return len(self.list)
    

if __name__=='__main__':
    x=Dequeue()
    x.insert_front(10)
    x.insert_rear(20)

    try:
        # print(f'Delete Element: {x.delete_front()}')
        # print(f'Delete Element: {x.delete_rear()}')
        print(f"Front Element: {x.get_front()}")
        print(f"Rear Element: {x.get_rare()}")
        print(f"Total Element: {x.size()}")
    except IndexError as e:
        print(e.args[0])
