# Course: CS261 - Data Structures
# Student Name: Michael Uchmanowicz
# Assignment: A4 P1
# Description: a BST class


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        if cur.left:
            self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        if cur.right:
            self._str_helper(cur.right, values)

    def add(self, value: object) -> None:
        """
        Adds new value to the tree, maintaining BST property. Duplicates must be
        allowed and placed in the right subtree
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            if value < self.root.value and self.root.left is None:
                self.root.left = TreeNode(value)
            elif value > self.root.value and self.root.right is None:
                self.root.right = TreeNode(value)
            else:
                P = None
                N = self.root
                while N is not None:
                    P = N
                    if value < N.value:
                        N = N.left
                    else:
                        N = N.right
                if value < P.value:
                    P.left = TreeNode(value)
                else:
                    P.right = TreeNode(value)

    def contains(self, value: object) -> bool:
        """
        Returns True if the value parameter is in the BinaryTree or False if it is not in
        the tree. If the tree is empty, the method should return False
        """
        if self.root is None:
            return False
        else:
            if value < self.root.value and self.root.left is None:
                return False
            elif value > self.root.value and self.root.right is None:
                return False
            else:

                N = self.root
                while N is not None:

                    if N.value == value:
                        return True
                    elif value < N.value:
                        N = N.left
                    else:
                        N = N.right
                return False

    def get_first(self) -> object:
        """
        Returns the value stored at the root node. If the BinaryTree is empty, this
        method returns None.
        """
        if self.root is None:
            return None
        else:
            return self.root.value

    def remove_first(self) -> bool:
        """
        Removes the root node in the BinaryTree. Returns False if
        the tree is empty and there is no root node to remove and True if the root is removed
        """
        if self.root is None:
            return False
        else:
            N, PN, l_r = self.find(self.root.value)
            if self.root.right is None and self.root.left is None:
                self.root = None
                return True
            else:
                if N.right is None:
                    self.root = N.left
                    return True
                else:
                    S, PS = self.in_order_sucessor(N)
                    S.left = N.left
                    if S is not N.right:
                        PS.left = S.right
                        S.right = N.right
                    self.root = S
                    return True

    def remove(self, value) -> bool:
        """
        Remove the first instance of the object in the BinaryTree. The method
        must return True if the value is removed from the BinaryTree and otherwise return False
        """
        N, PN, l_r = self.find(value)
        if N is None:
            pass
        else:
            if N.left is None and N.right is None:
                if N == self.root:
                    self.root = None
                    return True
                if PN is not None:
                    if PN.left == N:
                        PN.left = None
                        return True
                    else:
                        PN.right = None
                        return True
            elif N.left is None:
                if PN is None:
                    self.root = N.right
                    return True
                else:
                    PN.right = N.left
                    return True
            elif N.right is None:
                if PN is None:
                    self.root = N.left
                    return True
                else:
                    PN.right = N.left
                    return True
            else:
                S, PS = self.in_order_sucessor(N)
                S.left = N.left
                if S is not N.right:
                    PS.left = S.right
                    S.right = N.right
                    if N == self.root:
                        self.root = S
                    return True
                if N == self.root:
                    self.root = S
                    return True
                if l_r == "l":
                    PN.left = S
                    return True
                else:
                    PN.right = S
                    return True

        return False

    def pre_order_traversal(self) -> Queue:
        """
        Performs pre-order transverse
        """

        N = self.root
        io = Queue()

        return self.preOrder(N, io)

    def preOrder(self, N, queue):
        """
        Helper function to perform pre-order traversal
        """
        if N is not None:
            queue.enqueue(N.value)
            self.preOrder(N.left, queue)
            self.preOrder(N.right, queue)
        return queue

    def in_order_traversal(self) -> Queue:
        """
        Performs in-order transverse
        """

        N = self.root
        io = Queue()

        return self.inOrder(N, io)

    def inOrder(self, N, queue):
        """
        Helper function to perform in-order traversal
        """
        if N is not None:
            self.inOrder(N.left, queue)
            queue.enqueue(N.value)
            self.inOrder(N.right, queue)
        return queue

    def post_order_traversal(self) -> Queue:
        """
        Performs post-order transverse
        """
        N = self.root
        io = Queue()

        return self.postOrder(N, io)

    def postOrder(self, N, queue):
        """
        Helper function to perform in-order traversal
        """
        if N is not None:
            self.postOrder(N.left, queue)
            self.postOrder(N.right, queue)
            queue.enqueue(N.value)
        return queue

    def by_level_traversal(self) -> Queue:
        """
        Performs By level transverse
        """
        sort = Queue()
        q = Queue()
        return self.traverse_level(sort, q)

    def traverse_level(self, queue, q):
        """
        By level traversal helper
        """
        sort = queue
        q = q

        q.enqueue(self.root)
        while not q.is_empty():
            N = q.dequeue()
            if N is not None:
                sort.enqueue(N.value)
                if N.left is not None:
                    q.enqueue(N.left)
                if N.right is not None:
                    q.enqueue(N.right)
        return sort

    def is_full(self) -> bool:
        """
        Returns True if the current tree is a ‘full binary tree’
        """
        return self.is_full_helper(self.root)

    def is_full_helper(self, N):
        """
        Helper function for is full function
        """

        if N is None:
            return True

        if N.left is None and N.right is None:
            return True

        if N.left is not None and N.right is not None:
            return self.is_full_helper(N.left) and self.is_full_helper(N.right)

        return False

    def is_complete(self) -> bool:
        """
        returns True if the current tree is a ‘complete binary tree’
        """
        size = self.size()
        index = 0
        return self.is_complete_helper(self.root, index, size)

    def is_complete_helper(self, N, index, size):
        """
        Helper function for is complete function
        """

        if N is None:
            return True

        if index >= size:
            return False

        return (self.is_complete_helper(N.left, 2 * index + 1, size)
                and self.is_complete_helper(N.right, 2 * index + 2, size)
                )

    def is_perfect(self) -> bool:
        """
        Returns True if the current tree is a ‘perfect binary tree’
        """
        height = self.height() + 1
        return self.is_perfect_helper(self.root, height)

    def is_perfect_helper(self, N, height, level=0):
        """
        Helper function for is perfect function
        """

        # An empty tree is perfect
        if N is None:
            return True

        if N.left is None and N.right is None:
            return height == level + 1

        if N.left is None or N.right is None:
            return False

        return self.is_perfect_helper(N.left, height, level + 1) and self.is_perfect_helper(N.right, height, level + 1)

    def size(self) -> int:
        """
        Returns the total number of nodes in the tree.
        """
        N = self.root

        return self.size_helper(N)

    def size_helper(self, node):
        """
        Helper function for size function
        """
        if node is None:
            return 0
        else:
            return self.size_helper(node.left) + 1 + self.size_helper(node.right)

    def height(self) -> int:
        """
        Returns the height of the binary tree. Empty tree has a height of -1.
        """
        return self.height_helper(self.root)

    def height_helper(self, N):
        """
        Helper function for the height tree
        """
        if N is None:
            return -1

        else:
            l_height = self.height_helper(N.left)
            r_height = self.height_helper(N.right)

            if l_height > r_height:
                return l_height + 1
            else:
                return r_height + 1

    def count_leaves(self) -> int:
        """
        Returns the number of nodes in the tree that have no children
        """
        return self.count_leaves_helper(self.root)

    def count_leaves_helper(self, N):
        """
        Helper function for count leaves
        """
        if N is None:
            return 0
        if N.left is None and N.right is None:
            return 1
        else:
            return self.count_leaves_helper(N.left) + self.count_leaves_helper(N.right)

    def count_unique(self) -> int:
        """
        Returns the count of unique values stored in the tree
        """
        values = self.in_order_traversal()
        total = 0
        if values.is_empty():
            return total
        first = values.dequeue()
        while not values.is_empty():
            second = values.dequeue()
            if first != second:
                total += 1
            first = second
        total += 1
        return total

    def find(self, value) -> object:
        """
        Find the first node with the value supplied
        """
        N = self.root
        PN = None
        l_r = None
        while N is not None:
            if N.value == value:
                return N, PN, l_r
            elif N.value > value:
                PN = N
                N = N.left
                l_r = "l"
            else:
                PN = N
                N = N.right
                l_r = "r"
        if N is None:
            return None, None, None
        else:
            return N, PN, l_r

    def in_order_sucessor(self, N) -> object:
        """
        Find a nodes in order successor and return that value
        """
        if N.right.left is None:
            return N.right, N
        else:
            N = N.right
            while N.left is not None:
                PS = N
                N = N.left
            return N, PS


# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    pass
    # """ add() example #1 """
    # # print("\nPDF - method add() example 1")
    # # print("----------------------------")
    # # tree = BST()
    # # print(tree)
    # # tree.add(10)
    # # tree.add(15)
    # # tree.add(5)
    # # print(tree)
    # # tree.add(15)
    # # tree.add(15)
    # # print(tree)
    # # tree.add(5)
    # # print(tree)
    #
    # """ add() example 2 """
    # # print("\nPDF - method add() example 2")
    # # print("----------------------------")
    # # tree = BST()
    # # tree.add(10)
    # # tree.add(10)
    # # print(tree)
    # # tree.add(-1)
    # # print(tree)
    # # tree.add(5)
    # # print(tree)
    # # tree.add(-1)
    # # print(tree)
    #
    # """ contains() example 1 """
    # # print("\nPDF - method contains() example 1")
    # # print("---------------------------------")
    # # tree = BST([10, 5, 15])
    # # print(tree.contains(15))
    # # print(tree.contains(-10))
    # # print(tree.contains(15))
    #
    # """ contains() example 2 """
    # # print("\nPDF - method contains() example 2")
    # # print("---------------------------------")
    # # tree = BST()
    # # print(tree.contains(0))
    #
    # """ get_first() example 1 """
    # # print("\nPDF - method get_first() example 1")
    # # print("----------------------------------")
    # # tree = BST()
    # # print(tree.get_first())
    # # tree.add(10)
    # # tree.add(15)
    # # tree.add(5)
    # # print(tree.get_first())
    # # print(tree)
    #
    # # """ remove() example 1 """
    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.remove(7))
    # print(tree.remove(15))
    # print(tree.remove(15))
    # # #
    # # # """ remove() example 2 """
    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.remove(20))
    # print(tree)
    # # #
    # # # """ remove() example 3 """
    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    # print(tree.remove(20))
    # print(tree)
    # # comment out the following lines
    # # if you have not yet implemented traversal methods
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())
    # #
    # # """ remove_first() example 1 """
    # # # print("\nPDF - method remove_first() example 1")
    # # # print("-------------------------------------")
    # # # tree = BST([10, 15, 5])
    # # # print(tree.remove_first())
    # # # print(tree)
    # #
    # # """ remove_first() example 2 """
    # # # print("\nPDF - method remove_first() example 2")
    # # # print("-------------------------------------")
    # # # tree = BST([10, 20, 5, 15, 17, 7])
    # # # print(tree.remove_first())
    # # # print(tree)
    # #
    # # """ remove_first() example 3 """
    # # # print("\nPDF - method remove_first() example 3")
    # # # print("-------------------------------------")
    # # # tree = BST([10, 10, -1, 5, -1])
    # # # tree = BST([10, 10, -1, 5, -1])
    # # # print(tree.remove_first(), tree)
    # # # print(tree.remove_first(), tree)
    # # # print(tree.remove_first(), tree)
    # # # print(tree.remove_first(), tree)
    # # # print(tree.remove_first(), tree)
    # # # print(tree.remove_first(), tree)
    #
    # """ remove_first() example 1 """
    # print("\nPDF - method remove_first() example 1")
    # print("-------------------------------------")
    # tree = BST([10, 15, 5])
    # print(tree.remove(10))
    # print(tree)
    #
    # # """ remove_first() example 2 """
    # print("\nPDF - method remove_first() example 2")
    # print("-------------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7])
    # print(tree.remove(10))
    # print(tree)
    # #
    # # """ remove_first() example 3 """
    # print("\nPDF - method remove_first() example 3")
    # print("-------------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.remove(10), tree)
    # print(tree.remove(10), tree)
    # print(tree.remove(-1), tree)
    # print(tree.remove(-1), tree)
    # print(tree.remove(5), tree)

    #
    # """ Traversal methods example 1 """
    # # print("\nPDF - traversal methods example 1")
    # # print("---------------------------------")
    # # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # # print(tree.pre_order_traversal())
    # # print(tree.in_order_traversal())
    # # print(tree.post_order_traversal())
    # # print(tree.by_level_traversal())
    #
    # """ Traversal methods example 2 """
    # # print("\nPDF - traversal methods example 2")
    # # print("---------------------------------")
    # # tree = BST([10, 10, -1, 5, -1])
    # # print(tree.pre_order_traversal())
    # # print(tree.in_order_traversal())
    # # print(tree.post_order_traversal())
    # # print(tree.by_level_traversal())
    #
    # """ Comprehensive example 1 """
    # # print("\nComprehensive example 1")
    # # print("-----------------------")
    # # tree = BST()
    # # header = 'Value   Size  Height   Leaves   Unique   '
    # # header += 'Complete?  Full?    Perfect?'
    # # print(header)
    # # print('-' * len(header))
    # # print(f'  N/A {tree.size():6} {tree.height():7} ',
    # #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    # #       f'{str(tree.is_complete()):10}',
    # #       f'{str(tree.is_full()):7} ',
    # #       f'{str(tree.is_perfect())}')
    #
    # # for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
    # #     tree.add(value)
    # #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    # #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    # #           f'{str(tree.is_complete()):10}',
    # #           f'{str(tree.is_full()):7} ',
    # #           f'{str(tree.is_perfect())}')
    # # print()
    # # print(tree.pre_order_traversal())
    # # print(tree.in_order_traversal())
    # # print(tree.post_order_traversal())
    # # print(tree.by_level_traversal())
    #
    # """ Comprehensive example 2 """
    # # print("\nComprehensive example 2")
    # # print("-----------------------")
    # # tree = BST()
    # # header = 'Value   Size  Height   Leaves   Unique   '
    # # header += 'Complete?  Full?    Perfect?'
    # # print(header)
    # # print('-' * len(header))
    # # print(f'N/A   {tree.size():6} {tree.height():7} ',
    # #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    # #       f'{str(tree.is_complete()):10}',
    # #       f'{str(tree.is_full()):7} ',
    # #       f'{str(tree.is_perfect())}')
    # #
    # # for value in 'DATA STRUCTURES':
    # #     tree.add(value)
    # #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    # #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    # #           f'{str(tree.is_complete()):10}',
    # #           f'{str(tree.is_full()):7} ',
    # #           f'{str(tree.is_perfect())}')
    # # print('', tree.pre_order_traversal(), tree.in_order_traversal(),
    # #       tree.post_order_traversal(), tree.by_level_traversal(),
    # #       sep='\n')
    #
    # print("\n Remove")
    # print("---------------------------------")
    # tree = BST([10])
    # print(tree.remove(7))
    # print(tree.remove(10))
    # print("---------------------------------")
    # tree = BST([])
    # print(tree.remove(7))
    # print(tree.remove(10))
    # # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.remove(10))
    # print(tree.in_order_traversal())
    # # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.remove(17))
    # print(tree.remove(5))
    # print(tree.remove(12))
    # print(tree.remove(7))
    # print(tree.in_order_traversal())
    # print(tree)
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.remove(17))
    # print(tree.remove(7))
    # print(tree.in_order_traversal())
    # print(tree)
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.remove(15))
    # print(tree.in_order_traversal())
    # print(tree)
    # #
    # tree = BST([10, 20])
    # print(tree.remove(20))
    #
    # tree = BST([10, 20])
    # print(tree.remove(10))
    #
    # tree = BST([10, 5])
    # print(tree.remove(5))
    # print(tree.remove(5))
    # print(tree.remove(5))
    # print(tree.remove(5))
    # tree = BST([10,11,12,13,14])
    # print(tree.remove(14))
    # print(tree.in_order_traversal())
    # print("---------------------")
    # tree = BST([20,10,30,9,11,25,31])
    # print(tree.remove(30))
    # print(tree.in_order_traversal())
    test_values = [20, 40, 10, 30, 34, 14, 24]
    test = BST()
    test.add(20)
    test.add(40)
    test.add(10)
    test.add(30)
    test.add(34)
    test.add(14)
    test.add(24)
    print(test)
    print(test.contains(40))
    print(test.remove(40))
    print(test.contains(40))
