from .linked_list import *


class OrderedList(LinkedList):
    def __init__(self):
        pass

    def add(self, data: int):
        temp = Node(data)
        if self.start is None:
            self.start = temp
        elif temp.data < self.start.data:
            temp.next = self.start
            self.start = temp
        else:
            node = self.start
            while node.next is not None and node.next.data < temp.data:
                node = node.next
            temp.next = node.next
            node.next = temp

        return self
