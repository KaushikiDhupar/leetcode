# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res=[]
        q=deque([root])

        while q:
            level_size=len(q)
            sum1=0
            for i in range(level_size):
                node=q.popleft()
                sum1=sum1+node.val
            

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sum1/level_size)
        return res



        