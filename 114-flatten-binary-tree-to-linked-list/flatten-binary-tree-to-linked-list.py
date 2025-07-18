# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def dfs(root):
            if not root:
                return None
            #recursively flatten the left and right subtree
            leftTail=dfs(root.left) #stores the last value found in left subtree
            rightTail=dfs(root.right) # stores the last value found in right subtree

            if root.left: #if the current root's left child subtree exist
                leftTail.right=root.right #connect the tail of the left subtree to the head of the right 

                root.right = root.left       # move the whole left subtree to the right
                #since in question we have to shift everything to right and have left as None

                root.left=None #reassign left to Null

            last=rightTail or leftTail or root #stores first truthy value  preferred if right tail value is last 
            #else left tail or else root
            return last 
        dfs(root) #main function call
        """
        Do not return anything, modify root in-place instead.
        """
        