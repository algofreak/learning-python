from lists.linked_list import LinkedList
from lists.ordered_list import OrderedList
from lists.doubly_linked_list import DoublyLinkedList
from lists.ordered_doubly_list import OrderedDoublyList


def main():
    list = (LinkedList() + 5 + 10 + 4 + 2 + 100 + 1000 + 45 + 38 + 39).add(99)
    print(f"LinkedList: {list}")
    list = list - 5
    print(f"LinkedList: {list}")

    list = (OrderedList() + 765764764 + 1 + 5 + 10 + 4 + 2 + 100 + 1000 + 45 + 38 + 39).add(99)
    print(f"OrderedList: {list}")
    list = list - 1
    print(f"OrderedList: {list}")

    list = (DoublyLinkedList(False) + 765764764 + 1 + 5 + 10 + 4 + 2 + 100 + 1000 + 45 + 38 + 39).add(99)
    print(f"DoublyLinkedList: {list}")
    list.set_reverse(True)
    list = list - 99
    print(f"DoublyLinkedList: {list}")

    list = (OrderedDoublyList(False) + 765764764 + 1 + 5 + 10 + 4 + 2 + 100 + 1000 + 45 + 38 + 39).add(99)
    print(f"OrderedDoublyList: {list}")
    # list.set_reverse(True)
    list = list - 100
    print(f"OrderedDoublyList: {list}")


if __name__ == '__main__':
    main()