from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]
        def search(root):
            if not root: return
            
            lca[0] = root

            if root.val > p.val and root.val > q.val:
                search(root=root.left)
            elif root.val < p.val and root.val < q.val:
                search(root=root.right)
            else:
                return

        search(root=root)
        return lca[0]
