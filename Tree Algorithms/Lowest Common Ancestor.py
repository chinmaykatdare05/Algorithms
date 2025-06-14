class TreeNode:
    """
    A Node in a Binary Tree.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    """
    Finds the Lowest Common Ancestor (LCA) of two nodes in a binary tree.

    Time complexity: O(n)
    Space complexity: O(h)  (h = height of the tree)

    :param root: TreeNode - Root node of the tree
    :param p: TreeNode - First node
    :param q: TreeNode - Second node
    :return: TreeNode - The LCA node
    """

    # Base case: If root is None, or we find one of the nodes, return root
    if root is None or root == p or root == q:
        return root

    # Recur on left and right subtrees
    left_lca = lowest_common_ancestor(root.left, p, q)
    right_lca = lowest_common_ancestor(root.right, p, q)

    # If we find nodes on both sides, current node is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise, return the non-null value (either left or right)
    return left_lca if left_lca else right_lca


# 🎯 **Example Usage**

# Build the binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Find LCA of nodes 5 and 1
lca_node = lowest_common_ancestor(root, root.left, root.right)
print(f"✅ LCA of 5 and 1: {lca_node.value}")  # Output: 3

# Find LCA of nodes 5 and 4
lca_node = lowest_common_ancestor(root, root.left, root.left.right.right)
print(f"✅ LCA of 5 and 4: {lca_node.value}")  # Output: 5
