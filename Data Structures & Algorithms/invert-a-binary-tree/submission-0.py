# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invertInline(root: Optional[TreeNode]):
            if not root:
                return 

            right = root.left
            invertInline(right)

            left = root.right
            invertInline(left)

            root.right = right
            root.left = left

        invertInline(root)
        return root