# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def moreReadable(preorder, inorder):
            if not preorder or not inorder: return None
            newNode = TreeNode(preorder[0])
            rootIndex = inorder.index(preorder[0])
            newNode.left = moreReadable(preorder[1: rootIndex+1], inorder[0: rootIndex])
            newNode.right = moreReadable(preorder[rootIndex+1:], inorder[rootIndex+1:])
            return newNode
        return moreReadable(preorder, inorder)