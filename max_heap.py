class BinaryMaxHeap:
    def __init__(self):
        self.heap=[None]*10
        self.size=0

    def getLeftChildIndex(self, index):
        return 2*index+1
    def getRightChildIndex(self, index):
        return 2*index+2

    def getParentIndex(self, index):
        return (index-1)//2

    def ensureCapacity(self):
        if self.size==len(self.heap):
            self.heap=self.heap+[None]*len(self.heap) #zdvojnasobenie kapacity

    def insert(self, value):
        self.ensureCapacity()
        self.heap[self.size]=value
        self.size+=1
        self.heapifyUp(self.size-1)

    def heapifyUp(self, index):
        while index>0:
            parentIndex=self.getParentIndex(index)
            if self.heap[index]>self.heap[parentIndex]:
                self.heap[index], self.heap[parentIndex]=self.heap[parentIndex], self.heap[index]
                index=parentIndex
            else:
                return


    def poll(self):
        if self.size==0:
            print("Heap is empty")
            return None
        self.heap[0],self.heap[self.size-1]=self.heap[self.size-1],self.heap[0]
        self.heap[self.size-1]=None
        self.size-=1
        self.heapifyDown(0)

    def heapifyDown(self, index):
        while self.getLeftChildIndex(index)<self.size:
            greaterChildIndex=self.getLeftChildIndex(index)
            if self.getRightChildIndex(index)<self.size and self.heap[self.getRightChildIndex(index)]>self.heap[greaterChildIndex]:
                greaterChildIndex=self.getRightChildIndex(index)
            if self.heap[index]<self.heap[greaterChildIndex]:
                self.heap[index], self.heap[greaterChildIndex]=self.heap[greaterChildIndex], self.heap[index]
                index=greaterChildIndex
            else:
                return

    def printHeap(self):
        print(self.heap[:self.size])
    def saveHeap(self):
        return(" ".join(map(str, self.heap[:self.size])))

    def draw(self, x, y, canvas):
        canvas.delete("all")
        if self.size > 0:
            self.draw_node(0, -1, -1, x, y, canvas, 150)
        else:
            print("Heap is empty")

    def draw_node(self, index, px, py, x, y, canvas, offset):
        if px != -1 and py != -1:
            canvas.create_line(px, py, x, y)

        left_child = self.getLeftChildIndex(index)
        right_child = self.getRightChildIndex(index)

        if left_child < self.size:
            self.draw_node(left_child, x, y, x - offset, y + 40, canvas, offset // 2)
        if right_child < self.size:
            self.draw_node(right_child, x, y, x + offset, y + 40, canvas, offset // 2)

        canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white")
        canvas.create_text(x, y, text=str(self.heap[index]))