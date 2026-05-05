class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)  # insertion of a new node
            else:
                self.left.insert(data)  # recursive call
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)  # insertion of a new node
            else:
                self.right.insert(data)  # recursive call
        # deletion of duplicate values

    def preorder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=" ")