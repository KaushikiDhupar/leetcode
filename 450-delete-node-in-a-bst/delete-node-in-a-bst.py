from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1: No child
            if not root.left and not root.right:
                return None
            # Case 2: One child
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 3: Two children
            else:
                # Find the inorder successor (smallest in right subtree)
                successor = self.getMinValueNode(root.right)
                root.val = successor.val  # Copy successor's value
                # Delete the successor node
                root.right = self.deleteNode(root.right, successor.val)

        return root

    def getMinValueNode(self, node: TreeNode) -> TreeNode:
        current = node
        while current.left:
            current = current.left
        return current
