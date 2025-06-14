class TreeNode:
    """
    Node class for AVL Tree.
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    AVL Tree with rotation balancing.

    Time Complexity:
        - Insertion: O(log n)
        - Deletion: O(log n)
        - Search: O(log n)
    Space Complexity:
        - O(n)
    """

    # Get height of the node
    def _height(self, node):
        return node.height if node else 0

    # Get balance factor
    def _get_balance(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    # Perform right rotation
    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    # Perform left rotation
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    # Insert a key and balance the tree
    def insert(self, node, key):
        # Perform normal BST insertion
        if not node:
            return TreeNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # Update the height of the node
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # Get the balance factor
        balance = self._get_balance(node)

        # Perform rotations to balance the tree
        # Left Heavy (Right Rotation)
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        # Right Heavy (Left Rotation)
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        # Left-Right Case
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right-Left Case
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # In-order traversal
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)


# 🎯 Example Usage
avl_tree = AVLTree()
root = None

for key in [10, 20, 30, 40, 50, 25]:
    root = avl_tree.insert(root, key)

print("In-order traversal of AVL tree:")
avl_tree.inorder(root)


class Node:
    """
    Node class for Red-Black Tree.
    """

    def __init__(self, key):
        self.key = key
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    """
    Red-Black Tree with insertion balancing.

    Time Complexity:
        - Insertion: O(log n)
        - Search: O(log n)
        - Deletion: O(log n)
    Space Complexity:
        - O(n)
    """

    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    # Left rotate
    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Right rotate
    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Fix the tree after insertion
    def _fix_insert(self, z):
        while z.parent and z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":
                    z.parent.color = y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._rotate_left(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self._rotate_right(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._rotate_right(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self._rotate_left(z.parent.parent)

        self.root.color = "BLACK"

    # Insert node
    def insert(self, key):
        node = Node(key)
        node.left = node.right = self.NIL
        y = None
        x = self.root

        while x != self.NIL:
            y = x
            x = x.left if node.key < x.key else x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        node.color = "RED"
        self._fix_insert(node)


# 🎯 Example Usage
rbt = RedBlackTree()
for num in [10, 20, 30, 15, 25]:
    rbt.insert(num)
