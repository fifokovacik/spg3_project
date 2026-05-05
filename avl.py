from avl_node import Node
class AVL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)
            self.update_root()

    def delete(self, value):
        if self.root is None:
            print("Tree is empty.")
            return

        if self.root.data == value and self.root.left is None and self.root.right is None:
            self.root = None
            return

        self.root.findNode(value)

        self.update_root()

    def update_root(self):
        if self.root is not None:
            while self.root.parent is not None:
                self.root = self.root.parent

    def inorder(self):
        if self.root is not None:
            self.root.inorder()
        else:
            print("Tree is empty")

    def preorder(self):
        if self.root is not None:
            self.root.preorder()
        else:
            print("Tree is empty")

    def postorder(self):
        if self.root is not None:
            self.root.postorder()
        else:
            print("Tree is empty")

    def draw(self, x, y, canvas):
        canvas.delete("all")
        if self.root is not None:
            self.root.draw(-1, -1, x, y, canvas)
        else:
            print("Tree is empty")