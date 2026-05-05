class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    def add(self, data):
        self.next=Node(data)