# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getLeftNodes(root): #calculate height of left subtree
            temp=root
            lh=0
            while temp:
                temp=temp.left
                lh+=1
            return lh
        def getRightNodes(root): #calculate height of right subtree
            temp=root
            rh=0
            while temp:
                temp=temp.right
                rh+=1
            return rh
        if not root:
            return 0
        lh=getLeftNodes(root)
        rh=getRightNodes(root)

        if lh==rh: # i.e the subtree is a perfect binary tree
            return (2**lh)-1
        return self.countNodes(root.left)+self.countNodes(root.right)+1 # else recursivesly call the function again to find the 
        # left subtree  where it is perfect binary tree and add it with right subtree and node where it is standing i.e 1 
        