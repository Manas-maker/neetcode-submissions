# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        minN = min(p.val, q.val)
        maxN = max(p.val, q.val)
        while curr.val<minN or curr.val>maxN:
            if p.val>curr.val:
                curr = curr.right
            else: curr = curr.left
        return curr