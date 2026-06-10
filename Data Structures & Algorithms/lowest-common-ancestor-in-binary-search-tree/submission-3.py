# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while (p.val-curr.val)*(q.val-curr.val)>0:
            if p.val>curr.val and q.val>curr.val:
                curr = curr.right
            else: curr = curr.left
        return curr