# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        inorder traversal and increment the count(by decreasing k value) when backtracking up
        from the leftmost node when k==0 we have the value of kth smallest
        O(log(n) + k) space: O(n): recursion stack
        """
        self.k=k
        self.ans=-1
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.k-=1
            if self.k==0:
                self.ans=node.val
                return
            inorder(node.right)
        inorder(root)
        return self.ans
        