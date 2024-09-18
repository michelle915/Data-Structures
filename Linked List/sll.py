# Name: Michelle Loya
# OSU Email: loyami@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 5/8/2021
# Description: This program implements a Singly Linked List data structure


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Adds a new node at the beginning of the list (right after the front sentinel)
        """
        new_node = SLNode(value)

        # If the list is not empty, insert the new node at the beginning
        if not self.is_empty():
            new_node.next = self._head.next

        # Update the head of the list to point to the new node
        self._head.next = new_node

    def insert_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list.
        """
        current = self._head

        while current.next is not None:
            current = current.next

        current.next = SLNode(value)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a new value at the specified index position [0, N] in the linked list.
        """
        if index < 0:
            raise SLLException
        elif index == 0:
            self.insert_front(value)
        else:
            new_node = SLNode(value)
            previous = None
            current = self._head.next

            for x in range(index):
                previous = current
                current = current.next

                if current is None and x != (index - 1):
                    raise SLLException

            if current is not None:
                new_node.next = previous.next
            previous.next = new_node

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node at the specified index position [0, N-1] from the linked list.
        """
        if index < 0 or self.is_empty():
            raise SLLException
        elif index == 0:
            self._head.next = self._head.next.next
        else:
            previous = None
            current = self._head.next

            for x in range(index):
                previous = current
                current = current.next

                if current is None and x != (index - 1):
                    raise SLLException

            if current is None:
                raise SLLException
            else:
                previous.next = previous.next.next

    def remove(self, value: object) -> bool:
        """
        This method traverses the list from the beginning to the end, and removes the first node
        that matches the provided “value” object. The method returns True if a node was removed
        from the list. Otherwise, it returns False.
        """
        if self.is_empty():
            return False
        else:
            previous = None
            current = self._head.next
            while current:
                if current.value == value:
                    if previous:
                        previous.next = previous.next.next
                    else:
                        self._head.next = current.next
                    return True
                previous = current
                current = current.next
            return False

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that match the provided “value”
        object. The method then returns this number.
        """
        count = 0

        node = self._head.next
        while node:
            if node.value == value:
                count += 1
            node = node.next

        return count

    def find(self, value: object) -> bool:
        """
        Returns a Boolean value based on whether or not the provided “value” object
        exists in the list.
        """
        node = self._head.next
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Returns a new LinkedList object that contains the requested number of nodes
        from the original list, starting with the node located at the requested start index. If the
        original list contains N nodes, a valid start_index is in range [0, N - 1] inclusive.
        """
        if start_index < 0 or size < 0 or start_index >= self.length() or (start_index + size) > self.length():
            raise SLLException
        elif size == 0:
            return LinkedList()
        else:
            new_list = LinkedList()
            new_list_size = 0
            new_list_current = new_list._head

            node = self._head.next
            current_index = 0

            while node:
                if current_index >= start_index:
                    new_node = SLNode(node.value)
                    new_list_current.next = new_node
                    new_list_current = new_list_current.next
                    new_list_size += 1

                if new_list_size == size:
                    return new_list

                node = node.next
                current_index += 1


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
