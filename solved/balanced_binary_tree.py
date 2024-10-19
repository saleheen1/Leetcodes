from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       isTreeBalanced = [True]

       def checkBalanced(root):
           if not root: return 0

           left = checkBalanced(root=root.left)
           right = checkBalanced(root=root.right)
           diff = abs(left -right)

           height = max(left,right)

           if diff > 1:
               isTreeBalanced[0] = False
               return 0

           return 1 + height
       
       checkBalanced(root= root)
       return isTreeBalanced[0]


