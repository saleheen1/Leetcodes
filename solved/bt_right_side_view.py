from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        
        q = deque()
        q.append(root)
        res = []

        if not root: return res

        while q:
            n = len(q)
            rightMostValue = q[-1]
            res.append(rightMostValue.val)
            for i in range(n):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

        


