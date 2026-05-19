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
load_button = tkinter.Button(root, text="Load", command=lambda:load())
save_entry = tkinter.Entry(root, width=30)
save_button = tkinter.Button(root, text="Save", command=lambda:save())

#600x600 canvas -> 300-900, 0-600
#0-300, 0-600 - data structure type buttons
#900-1200, 0-600 - data structure specialized functions(buttons, entries; deleted after change of data structure), load and save entries and buttons
c=tkinter.Canvas(root,width=600,height=600, bg="white")

c.place(x=300)
stack_button.place(x=50, y=25)
queue_button.place(x=50, y=125)
bst_button.place(x=50, y=225)
avl_button.place(x=50, y=325)
max_heap_button.place(x=50, y=425)
min_heap_button.place(x=50, y=525)

load_entry.place(x=920, y=500)
load_button.place(x=1110, y=500)
save_entry.place(x=920, y=550)
save_button.place(x=1110, y=550)

def stack_open():
    global rn, special
    for obj in special:
        obj.destroy()
    c.delete("all")
    rn="Stack"

    stack_push_entry = tkinter.Entry(root, width = 30)
    stack_push_button = tkinter.Button(root, text="push", command=lambda:stack_push(stack_push_entry.get()))
    stack_pop_button = tkinter.Button(root, text="pop", command=lambda:stack_pop(), width=25)
    special = [stack_push_entry, stack_push_button, stack_pop_button]

    stack_push_entry.place(x=920, y=25)
    stack_push_button.place(x=1110, y=25)
    stack_pop_button.place(x=950, y=75)

def queue_open():
    global rn, special
    for obj in special:
        obj.destroy()
    c.delete("all")
    rn="Queue"

    enqueue_entry = tkinter.Entry(root, width = 30)
    enqueue_button = tkinter.Button(root, text="enqueue", command=lambda:enqueue_here(enqueue_entry.get()))
    dequeue_button = tkinter.Button(root, text="dequeue", command=lambda:dequeue_here(), width=25)
    special = [enqueue_entry, enqueue_button, dequeue_button]

    enqueue_entry.place(x=920, y=25)
    enqueue_button.place(x=1110, y=25)
    dequeue_button.place(x=950, y=75)

def bst_open():
    global rn, special
    for obj in special:
        obj.destroy()
    c.delete("all")
    rn="Binary Search Tree"
def avl_open():
    global rn, special
    for obj in special:
        obj.destroy()
    c.delete("all")
    rn="Auto-balancing BST"
def max_heap_open():
    global rn, special
    for obj in special:
        obj.destroy()
    c.delete("all")
    rn="Binary Max Heap"
def min_heap_open():
    global rn, special
    for obj in special:
        obj.destroy()
    c.delete("all")
    rn="Binary Min Heap"

def load():
    load_entry.get()
    pass
def save():
    save_entry.get()
    pass

def stack_draw():
    c.delete("all")
    start_y = 20
    current = stack.top
    while current:
        c.create_rectangle(200, start_y, 400, start_y + 20)
        c.create_text(300, start_y + 10, text=current.data)
        start_y = start_y + 40
        current = current.next
def stack_push(value):
    stack.push(value)
    stack_draw()
def stack_pop():
    stack.pop()
    stack_draw()

def queue_draw():
    c.delete("all")
    start_y = 20
    current = queue.front
    while current:
        c.create_rectangle(200, start_y, 400, start_y + 20)
        c.create_text(300, start_y + 10, text=current.data)
        start_y = start_y + 40
        current = current.next
def enqueue_here(value):
    queue.enqueue(value)
    queue_draw()
def dequeue_here():
    queue.dequeue()
    queue_draw()

special=[]
rn=""
stack=Stack()
queue=Queue()

root.mainloop()