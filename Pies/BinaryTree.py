class BinaryTreeNode:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def maxNode(self,z):
        while z.right != None:
            z = z.right
        return z

    def minNode(self,z):
        while z.left != None:
            z = z.left
        return z

    def Successor(self,z):
        if z.right != None:
            return self.minNode(z.right)
        else:
            y = z.parent
            while y != None and z == y.right:
                z = y
                y = y.parent
            return y

    def insertNode(self,z):

        x = self.root
        y = None

        while (x):
            y = x
            
            if z.key < x.key:
                x = x.left
            else: x = x.right

        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else: y.right = z


    def removeNode(self,z):
        
        z = self.searchTree(self.root,z.key)
        
        if z.left is None and z.right is None:  # Case 1: No children
            if z == self.root:
                self.root = None
            else:
                if z == z.parent.left:
                    z.parent.left = None
                else:
                    z.parent.right = None
        elif z.left is None:  # Case 2: One child (right)
            if z == self.root:
                self.root = z.right
                self.root.parent = None
            else:
                if z == z.parent.left:
                    z.parent.left = z.right
                else:
                    z.parent.right = z.right
                z.right.parent = z.parent
        elif z.right is None:  # Case 2: One child (left)
            if z == self.root:
                self.root = z.left
                self.root.parent = None
            else:
                if z == z.parent.left:
                    z.parent.left = z.left
                else:
                    z.parent.right = z.left
                z.left.parent = z.parent
        else:  # Case 3: Two children
            s = self.Successor(z)
            z.key = s.key  # Replace z's key with successor's key
            self.removeNode(s)  # Remove the successor

    def inorderWalk(self,root):

        x = root
        
        if x != None:
            self.inorderWalk(x.left)
            print(x.key)
            self.inorderWalk(x.right)

    def searchTree(self,x,k):
        while (x != None) and (k != x.key):
            if k < x.key:
                x = x.left
            else: x = x.right
            
        return x
            
        
                
        
t = BinaryTree()
n = BinaryTreeNode(9)
n2 = BinaryTreeNode(11)
n3 = BinaryTreeNode(7)
n4 = BinaryTreeNode(10)
n5 = BinaryTreeNode(5)
n6 = BinaryTreeNode(1)
n7 = BinaryTreeNode(22)


t.insertNode(n)
t.insertNode(n2)
t.insertNode(n3)
t.insertNode(n4)
t.insertNode(n5)
t.insertNode(n6)
t.insertNode(n7)

t.inorderWalk(n)

nextn = t.Successor(n3)

#print(nextn.key)

t.removeNode(n5)

t.inorderWalk(n)

#print(t.root.key)
#print(t.searchTree(n,7).key)
