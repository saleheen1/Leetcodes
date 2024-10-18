from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]

        def height(root):
            if not root: return 0

            left = height(root=root.left)
            right = height(root=root.right)

            diameter = left + right
            max_diameter[0] = max(max_diameter[0], diameter)
            return 1+ max(left,right)

        height(root= root)
        return max_diameter[0]
        