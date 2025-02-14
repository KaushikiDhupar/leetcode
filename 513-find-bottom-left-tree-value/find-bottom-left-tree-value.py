from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Edge case: Tree is empty
        
        q = deque([root])
        bottom_left = root.val  # Start with root value

        while q:
            level_size = len(q)
            for i in range(level_size):  # Process all nodes at current level
                node = q.popleft()

                # First node in this level is the leftmost one
                if i == 0:
                    bottom_left = node.val

                # Add left first, then right
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return bottom_left
