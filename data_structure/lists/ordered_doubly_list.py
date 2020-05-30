from .doubly_linked_list import *
# from .ordered_list import *


class OrderedDoublyList(DoublyLinkedList):
    def __init__(self, _reverse: bool):
        super().__init__(_reverse)

    def add(self, data: int):
        temp = DNode(data)
        if self.start is None:
            self.start = temp
            self.end = temp
        elif temp.data < self.start.data:
            temp.next = self.start
            self.start.prev = temp
            self.start = temp
        else:
            node = self.start
            while node.next is not None and node.next.data < temp.data:
                node = node.next
            temp.next = node.next
            if node.next is not None:
                node.next.prev = temp
            node.next = temp
            temp.prev = node

        return self
