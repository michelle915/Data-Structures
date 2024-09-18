# Name: Michelle Loya
# OSU Email: loyami@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: 5/30/23
# Description: This program implements a minheap.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    # parent: (index - 1) // 2
    # left child: 2 * index + 1
    # right child: 2 * index + 2

    def add(self, node: object) -> None:
        """
        This method adds a new object to the MinHeap while maintaining heap property.
        Runtime complexity: O(log N).
        """
        self._heap.append(node)

        new_node_index = (self.size() - 1)
        parent_index = (new_node_index - 1) // 2

        while new_node_index > 0 and self._heap[new_node_index] < self._heap[parent_index]:
            self._heap[new_node_index], self._heap[parent_index] = self._heap[parent_index], self._heap[new_node_index]

            new_node_index = parent_index
            parent_index = (new_node_index - 1) // 2

    def is_empty(self) -> bool:
        """
        This method returns True if the heap is empty; otherwise, it returns False.
        Runtime complexity: O(1).
        """
        if self._heap.is_empty():
            return True
        return False

    def get_min(self) -> object:
        """
        This method returns an object with the minimum key, without removing it from the heap. If
        the heap is empty, the method raises a MinHeapException.
        Runtime complexity: O(1).
        """
        if self.is_empty():
            raise MinHeapException
        return self._heap[0]

    def remove_min(self) -> object:
        """
        This method returns an object with the minimum key, and removes it from the heap. If the
        heap is empty, the method raises a MinHeapException.
        Runtime complexity: O(log N).
        """
        if self.is_empty():
            raise MinHeapException

        min = self._heap[0]

        self._heap[0] = self._heap[self.size() - 1]
        self._heap.remove_at_index(self.size() - 1)

        _percolate_down(self._heap, 0, self.size())

        return min

    def build_heap(self, da: DynamicArray) -> None:
        """
        This method receives a DynamicArray with objects in any order, and builds a proper
        MinHeap from them. The current content of the MinHeap is overwritten.
        Runtime complexity: O(N).
        """
        if da.length() == 0:
            self._heap = da
            return

        self._heap = da.slice(0, da.length())

        parent = (self.size() - 1) // 2

        while parent >= 0:
            _percolate_down(self._heap, parent, self.size())
            parent -= 1

    def size(self) -> int:
        """
        This method returns the number of items currently stored in the heap.
        The runtime complexity: O(1).
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        This method clears the contents of the heap.
        Runtime complexity: O(1).
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    Receives a DynamicArray and sorts its content in non-ascending order, using the Heapsort algorithm.
    Runtime complexity: O(N log N).
    """
    heap = MinHeap()
    heap.build_heap(da)

    # Move the smallest element to the end of the array, reduce heap size by 1 and percolate down the new root
    for k in range(heap.size() - 1, -1, -1):
        da[k] = heap.remove_min()


def _percolate_down(da: DynamicArray, parent_node: int, heap_size: int) -> None:
    """
    This method percolates a value down a heap if its value is greater than either of its children.
    For the downward percolation of the replacement node: if both children of the node have the same
    value (and are both smaller than the node), replacement node is swapped with the left child.
    """

    parent = parent_node
    percolate = True

    while percolate:
        l_child = 2 * parent + 1
        r_child = 2 * parent + 2
        smallest = parent

        if l_child < heap_size and da[l_child] < da[smallest]:
            smallest = l_child
        if r_child < heap_size and da[r_child] < da[smallest]:
            smallest = r_child

        if smallest != parent:
            da[parent], da[smallest] = da[smallest], da[parent]
            parent = smallest
        else:
            percolate = False


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
