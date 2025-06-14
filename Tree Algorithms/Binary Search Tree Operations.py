class TreeNode:
    """
    Node class for a Binary Search Tree (BST).
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree (BST) class with common operations.

    Time Complexities:
        - Insertion: O(log n) on balanced BSTs, O(n) on skewed
        - Search: O(log n) on balanced BSTs, O(n) on skewed
        - Deletion: O(log n) on balanced BSTs, O(n) on skewed
        - Traversal (Inorder, Preorder, Postorder): O(n)

    Space Complexity:
        - O(n) for storing nodes.
    """

    def __init__(self):
        self.root = None

    # 🚀 Insertion
    def insert(self, key):
        """
        Insert a new key into the BST.
        """
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """
        Helper function to insert a key recursively.
        """
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    # 🔍 Search
    def search(self, key):
        """
        Search for a key in the BST.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """
        Helper function for recursive search.
        """
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    # 🧹 Deletion
    def delete(self, key):
        """
        Delete a key from the BST.
        """
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        """
        Helper function to delete a node recursively.
        """
        if node is None:
            return node

        # Find the node to delete
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)

        return node

    # 🔢 Min/Max Value
    def min_value(self):
        """
        Find the minimum value node in the BST.
        """
        node = self._min_value_node(self.root)
        return node.key if node else None

    def _min_value_node(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current

    def max_value(self):
        """
        Find the maximum value node in the BST.
        """
        node = self.root
        while node and node.right:
            node = node.right
        return node.key if node else None

    # 🔄 Traversals
    def inorder(self):
        """
        Perform in-order traversal of the BST (Left -> Root -> Right).
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        """
        Helper function for in-order traversal.
        """
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def preorder(self):
        """
        Pre-order traversal (Root -> Left -> Right).
        """
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def postorder(self):
        """
        Post-order traversal (Left -> Right -> Root).
        """
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.key)


# 🎯 Example Usage

bst = BinarySearchTree()
elements = [50, 30, 70, 20, 40, 60, 80]

for elem in elements:
    bst.insert(elem)

print("In-order Traversal:", bst.inorder())
print("Pre-order Traversal:", bst.preorder())
print("Post-order Traversal:", bst.postorder())

# Search
print("Search for 40:", bst.search(40) is not None)

# Min/Max
print("Minimum value:", bst.min_value())
print("Maximum value:", bst.max_value())

# Deletion
bst.delete(50)
print("In-order after deleting 50:", bst.inorder())
