# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=deque([root])

        while q:
            rightSide=None # Tracks the last node encountered at the current level
            
            qlen=len(q)# Number of nodes in the current level
            for i in range(qlen):
                node=q.popleft() # Dequeue the next node in the current level
                if node:
                    rightSide=node # Update `rightSide` to the current node
                    q.append(node.left)# Add the left child to the queue for the next level
                    q.append(node.right)# Add the right child to the queue for the next level
            if rightSide:
                res.append(rightSide.val)# Add the value of the rightmost node to the result list
        return res