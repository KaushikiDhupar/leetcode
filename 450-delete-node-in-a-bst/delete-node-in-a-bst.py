from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == key:
            return self.helper(root)

        dummy = root
        curr = root

        while curr:
            if key < curr.val:
                if curr.left and curr.left.val == key:
                    curr.left = self.helper(curr.left)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = self.helper(curr.right)
                    break
                else:
                    curr = curr.right

        return dummy

    def helper(self, node: TreeNode) -> Optional[TreeNode]:
        # Case 1: No left child
        if node.left is None:
            return node.right
        # Case 2: No right child
        elif node.right is None:
            return node.left
        # Case 3: Two children
        else:
            # Find rightmost in left subtree
            right_child = node.right
            last_right = self.findLastRight(node.left)
            last_right.right = right_child
            return node.left

    def findLastRight(self, node: TreeNode) -> TreeNode:
        while node.right:
            node = node.right
        return node
