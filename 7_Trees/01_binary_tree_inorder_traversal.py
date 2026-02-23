# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Problem: 94. Binary Tree Inorder Traversal
        https://leetcode.com/problems/binary-tree-inorder-traversal/

        Intuition:
        - Fairly easy to write recursion
            - base case: if not root
        - Inorder is left, then current, right

        Time:
        - O(n)

        Space:
        - O(n)

        """

        res=[]
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return res

        