# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {val: idx for idx, val in enumerate(inorder)}
        self.idx = 0

        def construct(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.idx]
            self.idx += 1
            i = mp[root_val]

            root = TreeNode(root_val)
            root.left = construct(l, i - 1)
            root.right = construct(i + 1, r)
            return root

        return construct(0, len(preorder) - 1)
