# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque([root])
        res=[]

        while q:
            rightside=None
            qlen=len(q)
            for _ in range(qlen):
                node=q.popleft()
            
                if node:
                    rightside=node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if rightside:
                res.append(rightside.val)
        return res