from .linked_list import *


class DNode(Node):
    def __init__(self, data: int):
        super().__init__(data)
        self.prev = None


class DoublyLinkedList(LinkedList):
    start: DNode = None
    end: DNode = None

    def __init__(self, _reverse: bool):
        self.reverse = _reverse

    def set_reverse(self, _reverse: bool):
        self.reverse = _reverse

    def add(self, data: int):
        temp = DNode(data)
        if self.start is None:
            self.start = temp
        else:
            temp.prev = self.end
            self.end.next = temp
        self.end = temp

        return self

    def remove(self, data: int):
        if self.start is not None:
            node = self.start
            if node.data == data:
                self.start = self.start.next
                self.start.prev = None

            while node.next is not None and node.next.data != data:
                node = node.next

            if node.next is not None and node.next.data == data:
                if node.next == self.end:
                    self.end = node
                else:
                    node.next.prev = node

                node.next = node.next.next

        return self

    def direction_char(self):
        return '<->'

    def __str__(self):
        str = ""
        if self.reverse:
            node = self.end
            while node.prev is not None:
                str = str + f"[{node}] {self.direction_char()} "
                node = node.prev
        else:
            node = self.start
            while node.next is not None:
                str = str + f"[{node}] {self.direction_char()} "
                node = node.next
        str = str + f"[{node}]"
        return str

