# Definition for a binary tree node.
# Each node in the tree has a value, and pointers to its left and right children.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # This list will store the final result: values visible from the right side
        ds = []

        # Helper function to perform the recursive traversal
        def recursivefunc(node, level):
            # Base case: if the current node is None, stop going further
            if not node:
                return

            # If we are visiting this level for the first time,
            # it means this node is the rightmost node at this level
            if level == len(ds):
                ds.append(node.val)

            # First go to the right child (since we want right side view)
            recursivefunc(node.right, level + 1)
            
            # Then go to the left child
            recursivefunc(node.left, level + 1)

        # Start the recursive traversal from the root node at level 0
        recursivefunc(root, 0)

        # Return the list of values that are visible from the right side
        return ds
