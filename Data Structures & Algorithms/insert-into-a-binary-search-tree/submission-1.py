# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        newNode = TreeNode(val=val)
        if not root:
            return newNode
        while True:
            if val<curr.val:
                if not curr.left:
                    curr.left = newNode
                    break
                else:
                    curr = curr.left
                    continue
            else:
                if not curr.right:
                    curr.right =  newNode
                    break
                else:
                    curr = curr.right
                    continue
        return root