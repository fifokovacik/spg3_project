from stack_queue_node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.tail = None

    def enqueue(self, data):
        if self.front is None:
            self.front = Node(data)
            self.tail = self.front
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        elif self.front == self.tail:
            dequeued = self.front.data
            self.front = None
            self.tail = None
            return dequeued
        else:
            dequeued = self.front.data
            self.front = self.front.next
            return dequeued

    def printQueue(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def saveQueue(self):
        save=""
        current = self.front
        while current:
            save+=current.data+" "
            current = current.next
        return save