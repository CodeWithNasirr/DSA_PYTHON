class Node:
    def __init__(self,left=None,item=None,right=None):
        self.left=left
        self.item=item
        self.right=right


class BST:
    def __init__(self):
        self.root=None


    def insert(self,item):#3
        self.root=self.rinsert(self.root,item)

    def rinsert(self,root,item):
        if root is None:
            return Node(item=item)
        if item<root.item:
            root.left=self.rinsert(root.left,item)
        elif item>root.item:
            root.right=self.rinsert(root.right,item)
        return root



    def min(self,node):
        # current=self.root
        current=node
        while(current.left is not None):
            current=current.left
        return current.item

    #     result=[]
    #     self.r_min(self.root,result)
    #     return result[0]

    # def r_min(self,root,result):
    #     if root:
    #         self.r_min(root.left,result)
    #         result.append(root.item)

    def max(self,node):
        # current=self.root
        current=node
        while(current.right is not None):
            current=current.right
        return current.item
    #     result=[]
    #     self.r_max(self.root,result)
    #     return result[-1]
    # def r_max(self,root,result):
    #     if root:
    #         self.r_max(root.left,result)
    #         result.append(root.item)


    def deletion(self,node):
        self.root=self.r_deletion(self.root,node)

    def r_deletion(self,root,node):
        if root is None:
            return root
        if node<root.item:
            root.left=self.r_deletion(root.left)
        elif node>root.item:
            root.right=self.r_deletion(root.right)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item=self.min(root.right)#successer use here
            self.r_deletion(root.right,root.item)
            

if __name__=="__main__":
    x=BST()
    x.insert(50)
    x.insert(30)
    x.insert(40)
    x.insert(10)
    x.insert(90)
    x.insert(100)
    x.insert(60)
    x.deletion(90)
    print(f"minimum Element {x.min()}")
    print(f"Maximum Element {x.max()}")