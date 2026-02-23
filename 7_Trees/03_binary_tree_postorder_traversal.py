# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Problem: 145. Binary Tree Postorder Traversal
        https://leetcode.com/problems/binary-tree-postorder-traversal/

        Intuition:
        - first left, then right, then curr

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
            dfs(root.right)
            res.append(root.val)
        
        dfs(root)
        return res
        