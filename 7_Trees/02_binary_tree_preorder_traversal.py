# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Problem: 144. Binary Tree Preorder Traversal
        https://leetcode.com/problems/binary-tree-preorder-traversal/

        Intuition:
        - first curr, then left, then right

        Time:
        - O(n)

        Space:
        - O(n)

        """
        res=[]
        def dfs(root):
            if not root:
                return
            
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return res