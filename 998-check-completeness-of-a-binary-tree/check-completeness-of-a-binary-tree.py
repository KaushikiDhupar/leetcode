from collections import deque
from typing import Optional

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        flag = False  # Set to True when we see a None, indicating no more children should exist

        while q:
            node = q.popleft()

            if not node:
                flag = True  # If a None is found, set flag
            else:
                if flag:  
                    return False  # If we find a node after a None, it's not complete
                
                q.append(node.left)
                q.append(node.right)

        return True