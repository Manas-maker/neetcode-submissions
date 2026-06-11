# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def counter(root, maxVal):
            if root.val>=maxVal:
                nonlocal res
                res += 1
            if root.left: counter(root.left, max(maxVal, root.val))
            if root.right: counter(root.right, max(maxVal, root.val))
        counter(root, -100)
        return res