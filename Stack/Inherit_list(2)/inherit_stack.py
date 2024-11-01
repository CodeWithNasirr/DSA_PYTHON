class Stack(list):
    def is_empty(self):
        return len(self)== 0
    def push(self,item):
        self.append(item)
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError('Stack is Empty')

    def peak(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('Stack is Empty')
        
    def size(self):
        return len(self)
        
    def insert(self, index, object):
        raise AttributeError("No Attribute 'Insert' in Stack ")


if __name__=='__main__':
    x=Stack()
    x.push(10)
    x.push(20)
    x.push(30)
    x.push(40)
    x.insert(1,100)
    print(f"Top Element {x.peak()}")
    print(f"Delete Element {x.pop()}")
    print(f"Top Element {x.peak()}")
    print(f"Total Element {x.size()}")
    
