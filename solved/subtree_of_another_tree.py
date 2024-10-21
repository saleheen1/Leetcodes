from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p: Optional[TreeNode],q: Optional[TreeNode]):
            if not p and not q: return True
            if (p and not q) or (q and not p):
                return False
            
            if (p.val != q.val): return False
            return isSameTree(p=p.left, q= q.left) and isSameTree(p=p.right,q= q.right)
        
        def has_subtree(root:Optional[TreeNode]):
            if not root: return False
            if isSameTree(p=root,q=subRoot):
                return True
            
            return  has_subtree(root= root.left) or has_subtree(root= root.right)
        
        return has_subtree(root=root)

