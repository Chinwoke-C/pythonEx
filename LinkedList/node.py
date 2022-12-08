class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end="-> ")
            temp = temp.next
        print("None")

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if self.head.next is None:
            self.tail = self.head

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return

        self.tail.next = new_node
        self.tail = new_node


# lst = LinkedList()
# lst.append(4)
# lst.append(5)
# lst.append(9)
# print(lst.tail.value)
# print(lst.print_list())

lst = LinkedList()
lst.prepend(9)
lst.append(5)
lst.prepend(6)
print(lst.head.value)
print(lst.print_list())
