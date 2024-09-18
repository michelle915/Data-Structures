# Name: Michelle Loya
# OSU Email: loyami@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 4
# Due Date: 5/22/23
# Description: The following program implements a binary search tree (BST) class.


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        This method adds a new value to the tree. Duplicate values are allowed. If a node
        with that value is already in the tree, the new value is added to the right
        subtree of that node.
        """
        parent = None
        node = self._root

        while node is not None:
            parent = node
            if value < node.value:
                node = node.left
            else:
                node = node.right

        if parent is None:
            self._root = BSTNode(value)
        elif value < parent.value:
            parent.left = BSTNode(value)
        else:
            parent.right = BSTNode(value)

    def remove(self, value: object) -> bool:
        """
        This method removes a value from the tree. The method returns True if the value is
        removed. Otherwise, it returns False.
        """
        parent = None
        node = self._root

        while node is not None:
            if value == node.value:
                if node.left is not None and node.right is not None:
                    self._remove_two_subtrees(parent, node)
                elif node.left is not None or node.right is not None:
                    self._remove_one_subtree(parent, node)
                else:
                    self._remove_no_subtrees(parent, node)
                return True
            elif value < node.value:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right

        return False

    def _remove_no_subtrees(self, parent: BSTNode, node: BSTNode) -> None:
        """
        Removes node that has no subtrees (no left or right nodes)
        """
        if parent is None:
            self._root = None
        elif node.value < parent.value:
            parent.left = None
        else:
            parent.right = None

    def _remove_one_subtree(self, parent: BSTNode, node: BSTNode) -> None:
        """
        Remove nodes that has a left or right subtree (only)
        """
        successor = None
        if node.left is not None:
            successor = node.left
        else:
            successor = node.right

        if parent is None:
            self._root = successor
        elif node.value < parent.value:
            parent.left = successor
        else:
            parent.right = successor

    def _remove_two_subtrees(self, parent: BSTNode, node: BSTNode) -> None:
        """
        Removes node that has two subtrees.
        """
        # Find in order successor
        successor_parent = None
        successor = node.right
        while successor.left is not None:
            successor_parent = successor
            successor = successor.left

        if successor_parent is not None:
            successor_parent.left = successor.right
            successor.right = node.right
        successor.left = node.left

        if parent is None:
            self._root = successor
        elif node.value < parent.value:
            parent.left = successor
        else:
            parent.right = successor

    def contains(self, value: object) -> bool:
        """
        This method returns True if the value is in the tree. Otherwise, it returns False. If the tree is
        empty, the method returns False.
        """
        node = self._root

        while node is not None:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right

        return False

    def inorder_traversal(self) -> Queue:
        """
        This method will perform an inorder traversal of the tree and return a Queue object that
        contains the values of the visited nodes, in the order they were visited. If the tree is empty,
        the method returns an empty Queue.
        """
        node = self._root
        queue = Queue()

        return self.inorder_traversal_helper(node, queue)

    def inorder_traversal_helper(self, node, queue):
        """
        Helper function for inorder traversal.
        """
        if node is not None:
            self.inorder_traversal_helper(node.left, queue)
            queue.enqueue(node.value)
            self.inorder_traversal_helper(node.right, queue)
        return queue

    def find_min(self) -> object:
        """
        This method returns the lowest value in the tree. If the tree is empty, the method
        returns None.
        """
        if self.is_empty():
            return None

        node = self._root

        while node.left is not None:
            node = node.left

        return node.value

    def find_max(self) -> object:
        """
        This method returns the highest value in the tree. If the tree is empty, the method
        returns None.
        """
        if self.is_empty():
            return None

        node = self._root

        while node.right is not None:
            node = node.right

        return node.value

    def is_empty(self) -> bool:
        """
        This method returns True if the tree is empty. Otherwise, it returns False.
        """
        if self._root is None:
            return True
        return False

    def make_empty(self) -> None:
        """
        This method removes all of the nodes from the tree.
        """
        self._root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (44, 57, 32, 38, 54, 51),
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
