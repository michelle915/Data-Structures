# Name: Michelle Loya
# OSU Email: loyami@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 4
# Due Date: 5/22/23
# Description: The following program implements an AVL tree (one of several types of self-balancing BST) class.


import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        This method adds a new value to the tree while maintaining its AVL property. Duplicate
        values are not allowed.
        """
        parent = None
        node = self._root
        new_node = AVLNode(value)

        while node is not None:
            parent = node
            if value == node.value:
                return
            elif value < node.value:
                node = node.left
            else:
                node = node.right

        if parent is None:
            self._root = new_node
        elif value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.parent = parent

        while parent is not None:
            self._rebalance(parent)
            parent = parent.parent

    def remove(self, value: object) -> bool:
        """
        This method removes the value from the AVL tree. The method returns True if the value is
        removed. Otherwise, it returns False
        """
        parent = None
        node = self._root

        while node is not None:
            if value == node.value:
                if node.left is not None and node.right is not None:
                    parent = self._remove_two_subtrees(parent, node)
                elif node.left is not None or node.right is not None:
                    self._remove_one_subtree(parent, node)
                else:
                    self._remove_no_subtrees(parent, node)

                while parent is not None:
                    self._rebalance(parent)
                    parent = parent.parent

                while node is not None:
                    self._update_height(node)
                    node = node.parent

                return True
            elif value < node.value:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right

        return False

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

        if successor is not None:
            successor.parent = parent

    def _remove_two_subtrees(self, parent: AVLNode, node: AVLNode) -> AVLNode:
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
            if successor.right is not None:
                successor.right.parent = successor_parent
            successor.right = node.right
            node.right.parent = successor

        successor.left = node.left
        if node.left is not None:
            node.left.parent = successor

        if parent is None:
            self._root = successor
        elif node.value < parent.value:
            parent.left = successor
        else:
            parent.right = successor

        successor.parent = parent

        return successor if successor_parent is None else successor_parent

    def _balance_factor(self, node: AVLNode) -> int:
        """
        Returns the difference in height between a node’s right subtree and its left subtree
        """
        return self._get_height(node.right) - self._get_height(node.left)

    def _get_height(self, node: AVLNode) -> int:
        """
        Returns height of node.
        """
        if node is None:
            return -1
        return node.height

    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """
        This method implements a left rotation. The tree shifts counterclockwise and the parameter node moves
        downward in the tree, while its right child moves upward. The right child's left child will become the
        parameter node's new right child.
        """
        child = node.right
        node.right = child.left

        if node.right is not None:
            node.right.parent = node

        child.left = node
        node.parent = child

        self._update_height(node)
        self._update_height(child)

        return child

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """
        This method implements a right rotation. The tree shifts clockwise and the parameter node moves
        downward in the tree, while its left child moves upward. The left child's right child will become the
        parameter node's new left child.
        """
        child = node.left
        node.left = child.right

        if node.left is not None:
            node.left.parent = node

        child.right = node
        node.parent = child

        self._update_height(node)
        self._update_height(child)

        return child

    def _update_height(self, node: AVLNode) -> None:
        """
        Updates the height of a node
        """
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _rebalance(self, node: AVLNode) -> None:
        """
        This method performs rebalancing at each node
        """
        # Single right rotation if node is left heavy or double rotation (left then right) if
        # node's left child is right heavy
        if self._balance_factor(node) < -1:
            if self._balance_factor(node.left) > 0:
                node.left = self._rotate_left(node.left)
                node.left.parent = node
            old_parent = node.parent
            new_subtree_root = self._rotate_right(node)
            new_subtree_root.parent = old_parent

            if old_parent is None:
                self._root = new_subtree_root
            elif node == old_parent.left:
                old_parent.left = new_subtree_root
            else:
                old_parent.right = new_subtree_root

            node.parent = new_subtree_root

        # Single left rotation if node is right heavy or double rotation (right then left) if
        # node's right child is left heavy
        elif self._balance_factor(node) > 1:
            if self._balance_factor(node.right) < 0:
                node.right = self._rotate_right(node.right)
                node.right.parent = node
            old_parent = node.parent
            new_subtree_root = self._rotate_left(node)
            new_subtree_root.parent = old_parent

            if old_parent is None:
                self._root = new_subtree_root
            elif node == old_parent.left:
                old_parent.left = new_subtree_root
            else:
                old_parent.right = new_subtree_root

            node.parent = new_subtree_root

        # If no rotation at all is performed, updates node’s subtree height
        else:
            self._update_height(node)

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (42, 57, 49, 22, 75, 32, 88, 44, 47),
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(10):
        case = list(set(random.randrange(1, 200) for _ in range(90)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
