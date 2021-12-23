from _pytest import nodes
from stack_and_queue.stack_and_queue import Queue

class K_Node:
    def __init__(self,value):
        self.value = value
        self.children = []

class K_tree:
    def __init__(self, root = None, k = 0):
        self.root = root
        self.k = k


def fizz_test(val):
    fizz = K_Node("Fizz")
    buzz = K_Node("Buzz")
    fizz_buzz = K_Node("FizzBuzz")
    no_change = K_Node(val)
    if val[0] % 3 == 0 and val.value % 5 == 0:
        return fizz_buzz
    if val[0] % 3 == 0:
        return fizz
    if val[0] % 5 == 0:
        return buzz
    else:
        return no_change

# def new_tree(nodes_list):
#     new_tree = K_tree()
#     new_tree.root = nodes_list[0]
#     nodes_list.pop(0)
#     for node in nodes_list[]:


def tree_fizz_buzz(tree):
    q = Queue()
    root = tree.root
    if root is None:
        raise ValueError('Tree is empty!')
    q.enqueue(root)
    breadth_order = []
    while not q.is_empty():
        # immediately dequeue it
        dequeued = q.dequeue()
        tested = fizz_test(dequeued)
        breadth_order.append(tested)
        print(breadth_order)
        if dequeued.children:
            q.enqueue(dequeued.children[:])

    return breadth_order
