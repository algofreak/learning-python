class Node:
    data: int

    def __init__(self, _data):
        self.data = _data
        self.next = None


class LinkedList:
    start: Node = None
    current: Node = None

    def __init__(self):
        pass

    def __add__(self, data: int):
        return self.add(data)

    def __sub__(self, data: int):
        return self.remove(data)

    def direction_char(self):
        return '->'

    def __str__(self):
        str = ""
        node = self.start
        while node.next is not None:
            str = str + f"[{node.data}] {self.direction_char()} "
            node = node.next
        str = str + f"[{node.data}]"
        return str

    def add(self, data: int):
        temp = Node(data)
        if self.start is None:
            self.start = temp
        else:
            self.current.next = temp
        self.current = temp
        return self

    def remove(self, data: int):
        if self.start is not None:
            node = self.start
            if node.data == data:
                self.start = self.start.next

            while node.next is not None and node.next.data != data:
                node = node.next

            if node.next is not None and node.next.data == data:
                node.next = node.next.next

        return self

    def iterate(self):
        i = 0
        node = self.start
        while node is not None:
            print(f"{i} : {node.data}")
            node = node.next
            i += 1


def main():
    list = (LinkedList() + 5 + 10 + 4 + 2 + 100 + 1000 + 45 + 38 + 39).add(99)
    print(list)


if __name__ == '__main__':
    main()
