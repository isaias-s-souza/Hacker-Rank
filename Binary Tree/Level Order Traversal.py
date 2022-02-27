class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
global saida
saida = ''
def levelOrder(root, oqueimprimir = saida):
    #Write your code here
    if root.right == None and root.left == None:
        saida = oqueimprimir
    else:
        if not root.left is None:
            oqueimprimir += str(root.left.info) + ' '
            levelOrder(root.left)
        if not root.right is None:
            oqueimprimir += str(root.right.info) + ' '
            levelOrder(root.right)
print(saida[:-2])

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)