# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = collections.defaultdict(list)
        
        def traverse(node, level):
            if node is None:
                return

            if level % 2 == 1:
                levels[level].append(node.val)
                
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
            
        def rtraverse(node, level):
            if node is None:
                return

            if level % 2 == 1:
                node.val = levels[level].pop()
            rtraverse(node.left, level + 1)
            rtraverse(node.right, level + 1)
        
        traverse(root, 0)
        rtraverse(root, 0)
        
        return root