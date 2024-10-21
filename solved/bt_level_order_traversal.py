
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append(root)
        result = []

        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                popped = queue.popleft()
                level.append(popped.val)

                if popped.left: queue.append(popped.left)
                if popped.right: queue.append(popped.right)

            result.append(level)
        
        return result

        