class Node:#1
    def __init__(self,left=None,item=None,right=None):
        self.left=left
        self.item=item
        self.right=right


class BST:#2
    def __init__(self):
        self.root=None
        self.index_item=0

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



    def search(self,node):#4
        return self.research(self.root,node)
    
    def research(self,root,node):
        if root is None or node==root.item:
            return root
        if node<root.item:
            self.research(root.left,node)
        else:
            self.research(root.right,node)

    def inorder(self):#5
        result=[]
        self.r_inorder(self.root,result)
        return result
    
    def r_inorder(self,root,result):#5
        if root:
            self.r_inorder(root.left,result)
            result.append(root.item)
            self.r_inorder(root.right,result)
        
    def preorder(self):#6
        result=[]
        self.r_preorder(self.root,result)
        return result
    
    def r_preorder(self,root,result):#6
        if root:
            result.append(root.item)
            self.r_preorder(root.left,result)
            self.r_preorder(root.right,result)

    def postorder(self):#7
        result=[]
        self.r_postorder(self.root,result)
        return result
    
    def r_postorder(self,root,result):#7
        if root:
            self.r_postorder(root.left,result)
            self.r_postorder(root.right,result)
            result.append(root.item)

        
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
            root.left=self.r_deletion(root.left,node)#yaha per if&elif ka ager self.r_delection recurion hoker same delete pe point karega to root.left=same value means
        elif node>root.item:
            root.right=self.r_deletion(root.right,node)
        else:
            if root.left is None:   
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.item=self.min(root.right)#successer use here
            # Delete the inorder successor
            root.right=self.r_deletion(root.right,root.item)
            # self.r_deletion(root.right,root.item)
        return root
    
    def size(self):
        return len(self.inorder())



if __name__=="__main__":
    x=BST()
    x.insert(50)
    x.insert(30)
    x.insert(40)
    x.insert(10)
    x.insert(80)
    x.insert(100)
    # x.insert(90)
    x.insert(60)
    # x.insert(70)
    
    # if x.search(50):
    #     print("Node with item 50 found.")
    # else:
    #     print("Node not found.")
    # print(f"The Delete ele is {x.deletion(80)}")
    print(f"in-order list {x.inorder()}")
    print(f"pre-order list {x.preorder()}")
    print(f"Post-order list {x.postorder()}")
    print(f"Size of list {x.size()}")




    