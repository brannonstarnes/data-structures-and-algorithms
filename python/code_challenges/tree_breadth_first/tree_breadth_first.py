from stack_and_queue.stack_and_queue import Queue

def breadth_first(tree):
    q = Queue()
    root = tree.root
    if root is None:
        raise ValueError('Tree is empty!')
    # enqueue root
    q.enqueue(root)
    # while queue is not empty
    breadth_order = []
    while not q.is_empty():
        # immediately dequeue it
        dequeued = q.dequeue()
        print(dequeued.value)
        breadth_order.append(dequeued.value)
        if dequeued.left:
            q.enqueue(dequeued.left)
        if dequeued.right:
            q.enqueue(dequeued.right)

    return breadth_order
