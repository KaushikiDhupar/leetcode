from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxlen = 0
        
        # Queue stores pairs of (node, index), like a complete binary tree
        q = deque([(root, 0)])  # index of root is 0

        while q:
            level_size = len(q)
            # Leftmost and rightmost indices at this level
            level_head_index = q[0][1]  # leftmost index (normalized)
            level_tail_index = q[-1][1]  # rightmost index

            # Width = right - left + 1
            maxlen = max(maxlen, level_tail_index - level_head_index + 1)

            for _ in range(level_size):
                node, index = q.popleft()
                # Normalize index to prevent overflow (by subtracting level_head_index)
                normalized_index = index - level_head_index

                if node.left:
                    q.append((node.left, 2 * normalized_index + 1))
                if node.right:
                    q.append((node.right, 2 * normalized_index + 2))

        return maxlen
