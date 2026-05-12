class BinaryMinHeap:
    def __init__(self):
        self.heap = [None] * 10
        self.size = 0

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def getParentIndex(self, index):
        return (index - 1) // 2

    def ensureCapacity(self):
        if self.size == len(self.heap):
            self.heap = self.heap + [None] * len(self.heap)

    def insert(self, value):
        self.ensureCapacity()
        self.heap[self.size] = value
        self.size += 1
        self.heapifyUp(self.size - 1)

    def heapifyUp(self, index):
        while index > 0:
            parentIndex = self.getParentIndex(index)
            if self.heap[index] < self.heap[parentIndex]:
                self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
                index = parentIndex
            else:
                return

    def poll(self):
        if self.size == 0:
            print("Heap is empty")
            return None

        min_value = self.heap[0]

        self.heap[0] = self.heap[self.size - 1]
        self.heap[self.size - 1] = None
        self.size -= 1
        self.heapifyDown(0)

        return min_value

    def heapifyDown(self, index):
        while self.getLeftChildIndex(index) < self.size:
            smallerChildIndex = self.getLeftChildIndex(index)

            if self.getRightChildIndex(index) < self.size and self.heap[self.getRightChildIndex(index)] < self.heap[smallerChildIndex]:
                smallerChildIndex = self.getRightChildIndex(index)

            if self.heap[index] > self.heap[smallerChildIndex]:
                self.heap[index], self.heap[smallerChildIndex] = self.heap[smallerChildIndex], self.heap[index]
                index = smallerChildIndex
            else:
                return