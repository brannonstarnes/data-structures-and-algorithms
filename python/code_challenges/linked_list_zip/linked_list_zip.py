# if __name__ == "__main__" :

class Node():

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList():

    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        self.head = Node(value, self.head)


def zip_lists(list_1, list_2):
    current_1 = list_1.head
    current_2 = list_2.head

    if current_1 is None or current_2 is None:
        raise Exception(ValueError)

    while current_2:
        temp = current_1.next
        current_1.next = Node(current_2.value, temp)
        current_1 = current_1.next.next #(does this work?)
        if current_2.next:
            current_2 = current_2.next
        else:
            return list_1

# list1 = LinkedList()
# list1.insert("C")
# list1.insert("B")
# list1.insert("A")

# list2 = LinkedList()
# list2.insert("3")
# list2.insert("2")
# list2.insert("1")

# zipped = zip_lists(list1, list2)
# print(zipped.head.value, zipped.head.next.value, zipped.head.next.next.value, zipped.head.next.next.next.value, zipped.head.next.next.next.next.value, zipped.head.next.next.next.next.next.value)
