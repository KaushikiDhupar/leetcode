# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        res=[]
        q=deque()
        q.append(root)
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
            res.append(sum1)

                
        if k>len(res):
            return -1
        else:
            res.sort(reverse=True)
            return res[k-1]


        


        
        

        