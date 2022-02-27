import sys
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 

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

def height(root):
    if root is None:
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    max_height = max(rightHeight, leftHeight)
    return max_height + 1

tree = BinarySearchTree()

todaentrada = sys.stdin.read().split("\n")
t = int(todaentrada[0])
arr = list(map(int, todaentrada[1].split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root) - 1)
