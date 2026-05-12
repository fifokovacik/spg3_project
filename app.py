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
root2 = tkinter.Tk()
root2.title("Data structure visualisation")

def try1():
    try:
        root2.destroy()
    except:
        return

#600x600 canvas -> 300-900, 0-600
#0-300, 0-600 - data structure type buttons, load and save entries and buttons
#900-1200, 0-600 - data structure specialized functions(buttons, entries; deleted after change of data structure)
c=tkinter.Canvas(root,width=600,height=600, bg="white")
c.place(x=300)
try_button = tkinter.Button(root,text="Enter",command=try1)
try_button.place(x=10)

root.mainloop()