# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder=sorted(preorder) #property of bst that inorder of bst will always be sorted
        mp={val:ind for ind,val in enumerate(inorder)} #mapping element to index
    # so that when we find node that is current root in preoder we can have a fast look up to find its index in inorder
        self.ind=0

        def construct(l,r):
            if l>r:
                return None
            root_val=preorder[self.ind] # preorder is [node,left,right] so root of subtrees will always be the start
            self.ind += 1  # Move to next element in preorder
            i=mp[root_val] #find index of that node in inorder with map that maps value to ind value is key and ind is value
            root=TreeNode(root_val) #construct tree
            root.left=construct(l,i-1) #construct left tree by splitting from left of node found in inorder from left to i-1 
            root.right=construct(i+1,r) #construct right tree by splitting from right of node found in inorder from i+1 to right
            return root
        return construct(0,len(inorder)-1)

        