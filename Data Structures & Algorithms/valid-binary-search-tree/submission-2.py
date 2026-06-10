# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, minconstraint, maxconstraint):
            if not root:
                return True
            if (root.right and (root.right.val<=root.val or root.right.val>=maxconstraint)) or (root.left and (root.left.val>=root.val or root.left.val<=minconstraint)):
                return False 
            return check(root.left, minconstraint, root.val) and check(root.right, root.val, maxconstraint)
        return check(root, float('-inf'), float('inf'))