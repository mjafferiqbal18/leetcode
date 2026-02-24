# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Problem: 110. Balanced Binary Tree
        https://leetcode.com/problems/balanced-binary-tree/

        Intuition:
        - Regular code to return height, but check if lh,rh difference >1 or not

        Time:
        - O(n)

        Space:
        - O(1)
        
        """

        res = True
        def dfs(root):
            nonlocal res
            if not root:
                return 0

            lh = dfs(root.left)
            rh = dfs(root.right)
            if abs(lh-rh)>1:
                res=False
            
            return 1+max(lh,rh)
        dfs(root)
        return res
        