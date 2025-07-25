# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        self._leftmost_inorder(root)

    def _leftmost_inorder(self,node):
        while node:
            self.stack.append(node)
            node=node.left
    


        

    def next(self) -> int:
        top_Node=self.stack.pop() #top element will have smallest element
        #if the node has a right child process ots leftmost subtree
        if top_Node.right:
            self._leftmost_inorder(top_Node.right) #if right exist put in stack
        return top_Node.val
        

    def hasNext(self) -> bool:
        return len(self.stack)>0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()