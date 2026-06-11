# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
        def createTree(preorder, inorder):
            
            if len(preorder)>0 and len(inorder)>0:
                newNode = TreeNode(preorder[0])
                rootIndex = inorder.index(preorder[0])
                newNode.left = createTree(preorder[1:rootIndex+1], inorder[0:rootIndex])
                newNode.right = createTree(preorder[rootIndex+1:], inorder[rootIndex+1:])
                return newNode
            else: return None
        return createTree(preorder, inorder)
