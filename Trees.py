#Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
inorder(root)




#Binary Search Tree (BST)
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return BSTNode(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, val)

inorder(root)




#AVL Tree (Self-Balancing BST)
class AVLNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def insert(root, key):
    if not root:
        return AVLNode(key)
    elif key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    if balance > 1 and key < root.left.data:
        return right_rotate(root)
    if balance < -1 and key > root.right.data:
        return left_rotate(root)
    if balance > 1 and key > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and key < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = None
for val in [30, 20, 40, 10, 25, 50]:
    root = insert(root, val)

inorder(root)




#Find Maximum Element in a Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_max(root):
    if not root:
        return float('-inf')
    left_max = find_max(root.left)
    right_max = find_max(root.right)
    return max(root.data, left_max, right_max)

root = Node(10)
root.left = Node(20)
root.right = Node(5)
root.left.left = Node(30)

print("Maximum Element:", find_max(root))




#2. Count Number of Leaf Nodes in a Binary Tree
def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

print("Leaf Nodes Count:", count_leaves(root))




#3. Print All Root-to-Leaf Paths
def print_paths(root, path=[]):
    if not root:
        return
    path.append(root.data)
    if not root.left and not root.right:
        print(" -> ".join(map(str, path)))
    else:
        print_paths(root.left, path)
        print_paths(root.right, path)
    path.pop()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Root to Leaf Paths:")
print_paths(root)



