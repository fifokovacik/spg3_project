from stack_queue_node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode

    def isEmpty(self):
        return self.top is None

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:
            old = self.top
            self.top = self.top.next
            return old.data

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:
            return self.top.data

    def printStack(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()