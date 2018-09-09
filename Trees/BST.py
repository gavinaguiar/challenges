from Node import Node

class BST:
    bstMin = float("-inf")
    prev = bstMin
    def __init__(self):
        self.root = None
        
  
    def insert(self, curr, v):
        if not self.root:
            self.root = Node(v)
            return
        
        if v <= curr.value:
            if (curr.left):
                self.insert(curr.left,v)
            else:
                curr.left = Node(v)
        else:
            if (curr.right):
                self.insert(curr.right,v)
            else:
                curr.right = Node(v)
                
        
    def inorder(self,curr):
        if curr is None:
            return True
        self.inorder(curr.left)
        if self.prev <= curr.value:
            self.prev=curr.value
            #print curr.value
        else:
            return False
        self.inorder(curr.right)
        return True
        
        
    def checkBST(self):
        return self.inorder(bst.root)
    
    def findLargestAndItsParent(self, node):
        curr = node
        parent = None
        while curr.right is not None:
            parent = curr
            curr = curr.right            
        return curr, parent
    
    def findSecondLargest(self):
        largestNode, parent = self.findLargestAndItsParent(self.root)
        if largestNode.left is None:
            return parent.value;
        else:
            secondLargest, sparent = self.findLargestAndItsParent(largestNode.left)
            return secondLargest.value
            
myList = [3,1,5,7,8,6,4,0]
#myList = [5,3,1,4,8,7,12,10,9,11]
n=Node(10)
bst = BST()
for i in myList:
    bst.insert(bst.root,i)
l,p = bst.findLargestAndItsParent(bst.root)
print l.value , p.value
print bst.findSecondLargest()