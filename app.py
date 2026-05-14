import tkinter
from stack import Stack
from queue import Queue
from bst import BST
from avl import AVL
from max_heap import BinaryMaxHeap
from min_heap import BinaryMinHeap

root = tkinter.Tk()
root.title("Data structure visualisation")
root.geometry("1200x600")

stack_button = tkinter.Button(root, text="Stack", command=lambda:stack_open(), width=25)
queue_button = tkinter.Button(root, text="Queue", command=lambda:queue_open(), width=25)
bst_button = tkinter.Button(root, text="Binary Search Tree", command=lambda:bst_open(), width=25)
avl_button = tkinter.Button(root, text="Auto-balancing BST", command=lambda:avl_open(), width=25)
max_heap_button = tkinter.Button(root, text="Binary Max Heap", command=lambda:max_heap_open(), width=25)
min_heap_button = tkinter.Button(root, text="Binary Min Heap", command=lambda:min_heap_open(), width=25)

load_entry = tkinter.Entry(root, width=30)
load_button = tkinter.Button(root, text="Load", command=lambda:load(), width=5)
save_entry = tkinter.Entry(root, width=30)
save_button = tkinter.Button(root, text="Save", command=lambda:save(), width=5)

#600x600 canvas -> 300-900, 0-600
#0-300, 0-600 - data structure type buttons, load and save entries and buttons
#900-1200, 0-600 - data structure specialized functions(buttons, entries; deleted after change of data structure)
c=tkinter.Canvas(root,width=600,height=600, bg="white")

c.place(x=300)
stack_button.place(x=50, y=25)
queue_button.place(x=50, y=125)
bst_button.place(x=50, y=225)
avl_button.place(x=50, y=325)
max_heap_button.place(x=50, y=425)
min_heap_button.place(x=50, y=525)

load_entry.place(x=920, y=500)
load_button.place(x=1100, y=500)
save_entry.place(x=920, y=550)
save_button.place(x=1100, y=550)

def stack_open():
    pass
def queue_open():
    pass
def bst_open():
    pass
def avl_open():
    pass
def max_heap_open():
    pass
def min_heap_open():
    pass

def load():
    load_entry.get()
    pass
def save():
    save_entry.get()
    pass

root.mainloop()