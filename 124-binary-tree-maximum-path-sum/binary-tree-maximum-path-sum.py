# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float('-inf')  # ✅ use negative infinity

        def solve(node):
            if not node:
                return 0

            left = max(solve(node.left), 0)   # ✅ ignore negative paths
            right = max(solve(node.right), 0)

            left_plus_right_sum = left + right + node.val  # ✅ use node.val instead of root.val
            self.maxsum = max(self.maxsum, left_plus_right_sum)  # ✅ update class-level maxsum

            return node.val + max(left, right)  # ✅ return only one side + node

        solve(root)
        return self.maxsum
