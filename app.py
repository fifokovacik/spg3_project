import tkinter
from stack import Stack
from my_queue import Queue
from bst import BST
from avl import AVL
from max_heap import BinaryMaxHeap
from min_heap import BinaryMinHeap

root = tkinter.Tk()
root.title("Data structure visualisation")
root.geometry("1200x600")

stack_button = tkinter.Button(root, text="Stack", command=lambda:stack_open(), width=25)
queue_button = tkinter.Button(root, text="Queue", command=lambda:queue_open(), width=25)
bst_button = tkinter.Button(root, text="BST", command=lambda:bst_open(), width=25)
avl_button = tkinter.Button(root, text="AVL", command=lambda:avl_open(), width=25)
max_heap_button = tkinter.Button(root, text="Binary Max Heap", command=lambda:max_heap_open(), width=25)
min_heap_button = tkinter.Button(root, text="Binary Min Heap", command=lambda:min_heap_open(), width=25)

load_entry = tkinter.Entry(root, width=30)
load_button = tkinter.Button(root, text="Load", command=lambda:load())
save_entry = tkinter.Entry(root, width=30)
save_button = tkinter.Button(root, text="Save", command=lambda:save())

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

def stack_open(data=None):
    global rn, special
    for obj in special:
        obj.destroy()
    c.delete("all")
    rn=0

    stack_push_entry = tkinter.Entry(root, width = 30)
    stack_push_button = tkinter.Button(root, text="push", command=lambda:stack_push(stack_push_entry.get()))
    stack_pop_button = tkinter.Button(root, text="pop", command=lambda:stack_pop(), width=25)
    stack_print_button = tkinter.Button(root, text="print", command=lambda:stack.printStack(), width=25)
    special = [stack_push_entry, stack_push_button, stack_pop_button, stack_print_button]

    stack_push_entry.place(x=920, y=25)
    stack_push_button.place(x=1110, y=25)
    stack_pop_button.place(x=950, y=75)
    stack_print_button.place(x=950, y=125)

    if data is not None:
        stack.top = None
        for value in reversed(data):  #reversed so the top stays accurate
            stack_push(value)


def queue_open(data=None):
    global rn, special
    for obj in special:
        obj.destroy()
    c.delete("all")
    rn=1

    queue_enqueue_entry = tkinter.Entry(root, width = 30)
    queue_enqueue_button = tkinter.Button(root, text="enqueue", command=lambda:queue_enqueue(queue_enqueue_entry.get()))
    queue_dequeue_button = tkinter.Button(root, text="dequeue", command=lambda:queue_dequeue(), width=25)
    queue_print_button = tkinter.Button(root, text="print", command=lambda:queue.printQueue(), width=25)
    special = [queue_enqueue_entry, queue_enqueue_button, queue_dequeue_button, queue_print_button]

    queue_enqueue_entry.place(x=920, y=25)
    queue_enqueue_button.place(x=1110, y=25)
    queue_dequeue_button.place(x=950, y=75)
    queue_print_button.place(x=950, y=125)

    if data is not None:
        queue.front = None
        queue.tail = None

        for value in data:
            if value.strip():
                queue_enqueue(value)


def bst_open(data=None):
    global rn, special
    for obj in special:
        obj.destroy()
    c.delete("all")
    rn=2

    bst_insert_entry = tkinter.Entry(root, width = 30)
    bst_insert_button = tkinter.Button(root, text="insert", command=lambda:bst_insert(bst_insert_entry.get()))
    bst_preorder_button = tkinter.Button(root, text="print preorder", command=lambda:bst.preorder(), width=25)
    bst_inorder_button = tkinter.Button(root, text="print inorder", command=lambda:bst.inorder(), width=25)
    bst_postorder_button = tkinter.Button(root, text="print postorder", command=lambda:bst.postorder(), width=25)
    special = [bst_insert_entry, bst_insert_button, bst_preorder_button, bst_inorder_button, bst_postorder_button]

    bst_insert_entry.place(x=920, y=25)
    bst_insert_button.place(x=1110, y=25)
    bst_preorder_button.place(x=950, y=75)
    bst_inorder_button.place(x=950, y=125)
    bst_postorder_button.place(x=950, y=175)

    if data is not None:
        bst.root = None

        for value in data:
            if value.strip():
                bst_insert(value)


def avl_open(data=None):
    global rn, special
    for obj in special:
        obj.destroy()
    c.delete("all")
    rn=3

    avl_insert_entry = tkinter.Entry(root, width = 30)
    avl_insert_button = tkinter.Button(root, text="insert", command=lambda:avl_insert(avl_insert_entry.get()))
    avl_delete_entry = tkinter.Entry(root, width = 30)
    avl_delete_button = tkinter.Button(root, text="delete", command=lambda:avl_delete(avl_delete_entry.get()))
    avl_preorder_button = tkinter.Button(root, text="print preorder", command=lambda:avl.preorder(), width=25)
    avl_inorder_button = tkinter.Button(root, text="print inorder", command=lambda:avl.inorder(), width=25)
    avl_postorder_button = tkinter.Button(root, text="print postorder", command=lambda:avl.postorder(), width=25)
    special = [avl_insert_entry, avl_insert_button, avl_delete_entry, avl_delete_button, avl_preorder_button, avl_inorder_button, avl_postorder_button]

    avl_insert_entry.place(x=920, y=25)
    avl_insert_button.place(x=1110, y=25)
    avl_delete_entry.place(x=920, y=75)
    avl_delete_button.place(x=1110, y=75)
    avl_preorder_button.place(x=950, y=125)
    avl_inorder_button.place(x=950, y=175)
    avl_postorder_button.place(x=950, y=225)

    if data is not None:
        avl.root = None

        for value in data:
            if value.strip():
                avl_insert(value)


def max_heap_open(data=None):
    global rn, special
    for obj in special:
        obj.destroy()
    c.delete("all")
    rn=4

    max_heap_insert_entry = tkinter.Entry(root, width = 30)
    max_heap_insert_button = tkinter.Button(root, text="insert", command=lambda:max_heap_insert(max_heap_insert_entry.get()))
    max_heap_poll_button = tkinter.Button(root, text="remove max", command=lambda:max_heap_poll(), width=25)
    max_heap_print_button = tkinter.Button(root, text="print array", command=lambda:max_heap.printHeap(), width=25)
    special = [max_heap_insert_entry, max_heap_insert_button, max_heap_poll_button, max_heap_print_button]

    max_heap_insert_entry.place(x=920, y=25)
    max_heap_insert_button.place(x=1110, y=25)
    max_heap_poll_button.place(x=950, y=75)
    max_heap_print_button.place(x=950, y=125)

    if data is not None:
        max_heap.size = 0
        max_heap.heap = [None] * 10

        for value in data:
            if value.strip():
                max_heap_insert(value)

def min_heap_open(data=None):
    global rn, special
    for obj in special:
        obj.destroy()
    c.delete("all")
    rn=5

    min_heap_insert_entry = tkinter.Entry(root, width = 30)
    min_heap_insert_button = tkinter.Button(root, text="insert", command=lambda:min_heap_insert(min_heap_insert_entry.get()))
    min_heap_poll_button = tkinter.Button(root, text="remove min", command=lambda:min_heap_poll(), width=25)
    min_heap_print_button = tkinter.Button(root, text="print array", command=lambda:min_heap.printHeap(), width=25)
    special = [min_heap_insert_entry, min_heap_insert_button, min_heap_poll_button, min_heap_print_button]

    min_heap_insert_entry.place(x=920, y=25)
    min_heap_insert_button.place(x=1110, y=25)
    min_heap_poll_button.place(x=950, y=75)
    min_heap_print_button.place(x=950, y=125)

    if data is not None:
        min_heap.size = 0
        min_heap.heap = [None] * 10

        for value in data:
            if value.strip():
                min_heap_insert(value)


def load():
    file_path = load_entry.get()

    if not file_path.endswith(".txt"):
        print("Insert the location of an existing file (ending in .txt).")
        return None

    try:
        with open(file_path, "r") as file:
            structure_index = int(file.readline().strip())
            data = file.readline().split()

        data_structure_loaders = [stack_open,queue_open,bst_open,avl_open,max_heap_open,min_heap_open]

        if 0 <= structure_index < len(data_structure_loaders):
            loaded_structure = data_structure_loaders[structure_index](data)
            return loaded_structure
        else:
            print(
                f"Error: Index {structure_index} does not match any data structure."
            )

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' could not be found.")
    except ValueError:
        print(
            "Error: Invalid data format. First line must be a valid integer."
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None


def get_tree_data(node):
    if node is None:
        return ""
    return str(node.data) + " " + get_tree_data(node.left) + get_tree_data(node.right)


def save():
    file_path = save_entry.get()

    if not file_path.endswith(".txt"):
        print("Insert valid file name (ending in .txt).")
        return

    global rn
    if rn == "":
        print("No data structure selected to save.")
        return

    save_actions = {0: stack.saveStack, 1: queue.saveQueue, 2: lambda: get_tree_data(bst.root), 3: lambda: get_tree_data(avl.root), 4: max_heap.saveHeap, 5: min_heap.saveHeap}

    if rn in save_actions:
        data_to_save = save_actions[rn]()
    else:
        print("Error: Unknown data structure index.")
        return

    try:
        with open(file_path, "w") as file:
            file.write(str(rn) + "\n")
            file.write(data_to_save.strip() + "\n")

        print(f"Data successfully saved to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while saving: {e}")


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
    if value!="":
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
def queue_enqueue(value):
    if value!="":
        queue.enqueue(value)
        queue_draw()
def queue_dequeue():
    queue.dequeue()
    queue_draw()


def bst_insert(value):
    try:
        bst.insert(int(value))  # insert value from entry
        bst.draw(300, 20, c)  # redraw tree after insertion
    except ValueError:
        print("Please enter a valid integer")


def avl_insert(value):
    try:
        avl.insert(int(value))  # insert value from entry
        avl.draw(300, 20, c)  # redraw tree after insertion
    except ValueError:
        print("Please enter a valid integer")
def avl_delete(value):
    try:
        avl.delete(int(value))
        avl.draw(300, 20, c)
    except ValueError:
        print("Please enter a valid integer")


def max_heap_insert(value):
    try:
        max_heap.insert(int(value))
        max_heap.draw(300, 20, c)
    except ValueError:
        print("Please enter a valid integer")

def max_heap_poll():
    max_heap.poll()
    max_heap.draw(300, 20, c)

def min_heap_insert(value):
    try:
        min_heap.insert(int(value))
        min_heap.draw(300, 20, c)
    except ValueError:
        print("Please enter a valid integer")

def min_heap_poll():
    min_heap.poll()
    min_heap.draw(300, 20, c)


special=[]
rn=""
stack=Stack()
queue=Queue()
bst=BST()
avl=AVL()
max_heap = BinaryMaxHeap()
min_heap = BinaryMinHeap()

root.mainloop()