# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q=deque([root])
        found_Null=False #first we will set our flag to false so when we first our null value we be able to set to false
        while q:
            node=q.popleft()
            if node:
                if found_Null:
                    return False
                q.append(node.left)
                q.append(node.right)
            else:
                found_Null=True

        return True
                


        