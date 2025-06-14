class TreeNode:
    """
    A Node in a Binary Tree.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_balanced(root):
    """
    Checks if a binary tree is height-balanced.

    Time complexity: O(n)
    Space complexity: O(h)

    :param root: TreeNode - Root node of the tree
    :return: bool - True if the tree is balanced, False otherwise
    """

    def check_height(node):
        """
        Recursively checks the height of the node's subtrees and ensures the difference is ≤ 1.
        Returns -1 if unbalanced.
        """
        if not node:
            return 0

        left_height = check_height(node.left)
        right_height = check_height(node.right)

        # If the subtree is unbalanced (-1 returned), propagate the failure
        if (
            left_height == -1
            or right_height == -1
            or abs(left_height - right_height) > 1
        ):
            return -1

        # Return the height of the current subtree
        return max(left_height, right_height) + 1

    # If height returns -1, the tree is unbalanced
    return check_height(root) != -1


# 🎯 **Example Usage**

# Build a balanced tree
balanced_root = TreeNode(1)
balanced_root.left = TreeNode(2)
balanced_root.right = TreeNode(3)
balanced_root.left.left = TreeNode(4)
balanced_root.left.right = TreeNode(5)
balanced_root.right.left = TreeNode(6)
balanced_root.right.right = TreeNode(7)

# Build an unbalanced tree
unbalanced_root = TreeNode(1)
unbalanced_root.left = TreeNode(2)
unbalanced_root.left.left = TreeNode(3)

print(f"✅ Is the first tree balanced? {is_balanced(balanced_root)}")
# Output: True

print(f"❌ Is the second tree balanced? {is_balanced(unbalanced_root)}")
# Output: False
