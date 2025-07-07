# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def back(root):
            if not root:
                return 0
            left=back(root.left)
            right=back(root.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1
        back(root)
        return self.diameter




        