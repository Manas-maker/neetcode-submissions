# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        val1 = p.val
        val2 = q.val
        while curr:
            val3 = curr.val
            if val3>val1 and val3>val2:
                curr = curr.left
            elif val3<val1 and val3<val2:
                curr = curr.right
            else:
                return curr