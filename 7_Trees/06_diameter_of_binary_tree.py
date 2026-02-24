# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Problem: 543. Diameter of Binary Tree
    https://leetcode.com/problems/diameter-of-binary-tree/

    Intuition:
    - Diameter can be max height from any node (and not necessarily max height from root)
    - that is what we record by taking max at each call

    Time:
    - O(n)

    Space:
    - O(1)

    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam=0
        
        def bfs(curr):
            if not curr:
                return 0
            
            l_h=bfs(curr.left)
            r_h=bfs(curr.right)
            
            if (l_h+r_h)>self.diam:

                self.diam=l_h+r_h
            
            return 1+max(l_h,r_h)
        
        bfs(root)
        return self.diam
        