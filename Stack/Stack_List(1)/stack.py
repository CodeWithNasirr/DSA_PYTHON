class Stack:
    def __init__(self):
        self.list=[]

    def isempty(self):
        return len(self.list)== 0
    
    def push(self,item):
        self.list.append(item)

    def pop(self):
        if not self.isempty():
            return self.list.pop()
        else:
            raise IndexError("Stack is Empty ")
        
    def peek(self):
        return self.list[-1]
    
    def size(self):
        return len(self.list())




if __name__=='__main__':
    x=Stack()
    x.push(10)
    x.push(20)
    x.push(30)
    x.push(40)
    print(f"Top Element: {x.peek()}")
    print(f'Remove Element {x.pop()}')
    print(f"Top Element: {x.peek()}")
    
