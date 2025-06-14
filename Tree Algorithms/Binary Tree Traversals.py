class TreeNode:
    """
    A Node in a Binary Tree.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    A Binary Tree supporting Pre-order, In-order, and Post-order traversals.
    """

    def __init__(self):
        self.root = None

    def pre_order(self, node):
        """
        Pre-order Traversal: Root → Left → Right

        Time complexity: O(n)
        Space complexity: O(h) (h = height of tree)
        """
        if node:
            print(node.value, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        """
        In-order Traversal: Left → Root → Right

        Time complexity: O(n)
        Space complexity: O(h)
        """
        if node:
            self.in_order(node.left)
            print(node.value, end=" ")
            self.in_order(node.right)

    def post_order(self, node):
        """
        Post-order Traversal: Left → Right → Root

        Time complexity: O(n)
        Space complexity: O(h)
        """
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end=" ")


# 🎯 **Example Usage**

# Create nodes
tree = BinaryTree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)
tree.root.right.left = TreeNode(6)
tree.root.right.right = TreeNode(7)

print("✅ Pre-order traversal:")
tree.pre_order(tree.root)
# Output: 1 2 4 5 3 6 7

print("\n✅ In-order traversal:")
tree.in_order(tree.root)
# Output: 4 2 5 1 6 3 7

print("\n✅ Post-order traversal:")
tree.post_order(tree.root)
# Output: 4 5 2 6 7 3 1
