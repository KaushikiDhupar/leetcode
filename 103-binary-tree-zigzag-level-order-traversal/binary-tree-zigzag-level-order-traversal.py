# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([root])

        res=[]
        left_to_right=True
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not left_to_right:
                level.reverse()
            res.append(level)
            left_to_right=not left_to_right

        return res
                

        