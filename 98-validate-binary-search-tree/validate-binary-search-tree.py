from typing import Optional

# Definition for a binary tree node.
# Note: You had a typo `_init_` — corrected to `__init__`.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):  # <-- Correct constructor
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to validate the BST
        def valid(node, left, right):
            if not node:
                return True  # An empty subtree is valid
            
            # The current node must be strictly greater than left bound
            # and strictly less than right bound
            if not (left < node.val < right):
                return False

            # Recursively check the left subtree and right subtree
            return (
                valid(node.left, left, node.val) and  # Left subtree: values < current node
                valid(node.right, node.val, right)    # Right subtree: values > current node
            )

        # Initial range is (-∞, ∞) for the root
        return valid(root, float('-inf'), float('inf'))
