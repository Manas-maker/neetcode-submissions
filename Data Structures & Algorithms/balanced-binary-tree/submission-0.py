# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def check(root):
            if not root:
                return (0, True)
            left = check(root.left)
            right = check(root.right)
            return (max(left[0], right[0])+1, left[1] and right[1] and abs(left[0]-right[0])<=1)
        return check(root)[1]
        