# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Problem: 226. Invert Binary Tree
        https://leetcode.com/problems/binary-tree-postorder-traversal/

        Intuition:
        - From the example, we can see that we'll need to invert top down, so thats what we do
            - We make left right, and right left
            - then recursively call the function on the left and right trees
        
        Time: 
        - O(n)

        Space:
        - O(1)

        """
        if not root:
            return
        
        temp=root.left
        root.left=root.right
        root.right=temp        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        