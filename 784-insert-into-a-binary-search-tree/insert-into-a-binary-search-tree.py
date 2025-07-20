# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr=root
        while True: # lopp can be exited with break statement after inserting
            if curr.val<=val:
                if curr.right: #we are not at the leaf
                    curr=curr.right #traverse to leaf
                else: #we are at the leaf
                    curr.right=TreeNode(val) #insert at the leaf because in bst only at the leaf insertion can take place 
                    break #exit the infinite loop after inserting
            else:
                if curr.left: #we are not at the leaf
                    curr=curr.left #traverse to leaf
                else: #we are at the leaf
                    curr.left=TreeNode(val)  #insert at the leaf because in bst only at the leaf insertion can take place 
                    break # exit the infinite loop after inserting
        return root


        
        
        