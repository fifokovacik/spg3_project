from bst_node import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)

    def preorder(self):
        if self.root:
            self.root.preorder()
            print()
        else:
            print("Tree is empty")
    def inorder(self):
        if self.root:
            self.root.inorder()
            print()
        else:
            print("Tree is empty")
    def postorder(self):
        if self.root:
            self.root.postorder()
            print()
        else:
            print("Tree is empty")