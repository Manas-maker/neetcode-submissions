# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def search(root, target):
            if not root:
                return False
            if root.val == target:
                return True
            else:
                if root.val>target: return search(root.left, target)
                else: return search(root.right, target)
        if root.val>=min(p.val, q.val) and root.val<=max(p.val, q.val):
            if search(root, p.val) and search(root, q.val): return root
        if min(p.val, q.val)>root.val: return self.lowestCommonAncestor(root.right, p, q)
        else: return self.lowestCommonAncestor(root.left, p, q)