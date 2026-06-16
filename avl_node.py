class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.balance = 0
        self.depth = 0
        self.parent = None

    def updateBalance(self):
        if self.left is None and self.right is None:
            self.balance = 0
            self.depth = 0
        elif self.left is not None and self.right is not None:
            self.balance = self.right.depth - self.left.depth
            self.depth = max(self.left.depth, self.right.depth) + 1
        elif self.left is not None:
            self.balance = -self.left.depth - 1
            self.depth = self.left.depth + 1
        else:
            self.balance = self.right.depth + 1
            self.depth = self.right.depth + 1

    def insert(self, value):
        if value < self.data:
            if self.left is None:
                self.left = Node(value)
                self.left.parent = self
            else:
                self.left.insert(value)
        elif value > self.data:
            if self.right is None:
                self.right = Node(value)
                self.right.parent = self
            else:
                self.right.insert(value)

        self.updateBalance()

        if self.balance < -1:
            if self.left.balance <= 0:
                self.rightRotation()
            else:
                self.leftRightRotation()
        elif self.balance > 1:
            if self.right.balance >= 0:
                self.leftRotation()
            else:
                self.rightLeftRotation()

    def delete(self):
        if self.left and self.right:
            if self.right.depth > self.left.depth:
                newSelf = self.right.minParent()
            else:
                newSelf = self.left.maxParent()

            self.data = newSelf.data
            newSelf.delete()
            return

        child = self.left if self.left else self.right

        if self.parent:
            if self.parent.left == self:
                self.parent.left = child
            else:
                self.parent.right = child

            if child:
                child.parent = self.parent


            self.parent.recUpdate()

        else:
            if child:
                self.data = child.data
                self.left = child.left
                self.right = child.right
                self.balance = child.balance
                self.depth = child.depth
                if self.left:
                    self.left.parent = self
                if self.right:
                    self.right.parent = self

    def findNode(self, value):
        if value == self.data:
            self.delete()
        elif self.right and value > self.data:
            self.right.findNode(value)
        elif self.left and value < self.data:
            self.left.findNode(value)
        else:
            print("Binary tree does not include node provided for deletion.")

    def minParent(self):
        if self.left:
            return self.left.minParent()
        return self

    def maxParent(self):
        if self.right:
            return self.right.maxParent()
        return self

    def recUpdate(self):
        self.updateBalance()
        if self.balance < -1:
            if self.left.balance <= 0:
                self.rightRotation()
            else:
                self.leftRightRotation()
        elif self.balance > 1:
            if self.right.balance >= 0:
                self.leftRotation()
            else:
                self.rightLeftRotation()

        if self.parent:
            self.parent.recUpdate()

    def rightRotation(self):
        original_parent = self.parent
        new_top = self.left

        self.left = new_top.right
        if self.left:
            self.left.parent = self

        new_top.right = self
        self.parent = new_top

        new_top.parent = original_parent
        if original_parent is not None:
            if original_parent.left == self:
                original_parent.left = new_top
            else:
                original_parent.right = new_top

        self.updateBalance()
        new_top.updateBalance()

    def leftRotation(self):
        original_parent = self.parent
        new_top = self.right

        self.right = new_top.left
        if self.right:
            self.right.parent = self

        new_top.left = self
        self.parent = new_top

        new_top.parent = original_parent
        if original_parent is not None:
            if original_parent.left == self:
                original_parent.left = new_top
            else:
                original_parent.right = new_top

        self.updateBalance()
        new_top.updateBalance()

    def leftRightRotation(self):
        self.left.leftRotation()
        self.rightRotation()

    def rightLeftRotation(self):
        self.right.rightRotation()
        self.leftRotation()

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right is not None:
            self.right.inorder()

    def preorder(self):
        print(self.data, end=" ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.data, end=" ")

    def draw(self, px, py, x, y, canvas, offset):
        if px != -1 and py != -1:
            canvas.create_line(px, py, x, y)
        if self.left is not None:
            self.left.draw(x, y, x - offset, y + 40, canvas, offset//2)
        if self.right is not None:
            self.right.draw(x, y, x + offset, y + 40, canvas, offset//2)
        canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white")
        canvas.create_text(x, y, text=str(self.data))
        canvas.create_text(x - 15, y - 17, text=str(self.depth))
        canvas.create_text(x + 15, y - 17, text=str(self.balance))