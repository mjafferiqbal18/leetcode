# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Problem: 104. Maximum Depth of Binary Tree
        https://leetcode.com/problems/maximum-depth-of-binary-tree/

        Intuition:
        - Essentially a post order traversal, base case is if not root, ret 0
            - You recurse on left and right and then return 1+ max(left,right) 

        Time:
        - O(n)

        Space:
        - O(1)
        """
        if not root:
            return 0
        
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        