class TreeNode:
    """
    Represents a node in a binary tree.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def morris_inorder_traversal(root):
    """
    Performs an inorder traversal using Morris Traversal (without recursion or stack).

    Time complexity: O(n)
    Space complexity: O(1)

    :param root: TreeNode - Root of the binary tree
    :return: List[int] - Inorder traversal of the tree
    """
    result = []
    current = root

    while current:
        # If the left child is None, print current node and move to right child
        if current.left is None:
            result.append(current.value)
            current = current.right
        else:
            # Find the inorder predecessor (rightmost node of the left subtree)
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            # If the right child of the predecessor is None, create a temporary link to current
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                # Revert the temporary link and visit the current node
                predecessor.right = None
                result.append(current.value)
                current = current.right

    return result


# 🎯 **Example Usage**

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("🌟 Morris Inorder Traversal:", morris_inorder_traversal(root))
# Output: [4, 2, 5, 1, 6, 3, 7]
