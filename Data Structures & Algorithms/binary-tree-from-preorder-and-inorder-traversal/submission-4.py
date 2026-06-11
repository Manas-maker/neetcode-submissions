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
        def createTree(pl, pr, il, ir):
            
            if (pr-pl)>0 and (ir-il)>0:
                newNode = TreeNode(preorder[pl])
                rootIndex = hashmap[preorder[pl]]
                leftSize = rootIndex - il
                newNode.left = createTree(pl+1, leftSize + pl + 1, il, rootIndex)
                newNode.right = createTree(leftSize + pl + 1, pr, rootIndex+1, ir)
                return newNode
            else: return None
        return createTree(0, len(preorder), 0, len(inorder))
