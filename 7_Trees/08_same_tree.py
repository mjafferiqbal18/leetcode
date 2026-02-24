# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Problem: 100. Same Tree
    https://leetcode.com/problems/same-tree/

    Intuition:
    - You start a regular traversal and check:
        - if both roots exist, you make sure val same
            - else return false if one exists and the other doesnt
        - Then recurse on left and right 
    
    Time:
    - O(p+q)

    Space:
    - O(1)
    
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame=True
        
        def bfs(t1,t2):
            #base case:
            if not t1 and not t2:
                return
            elif not t1 or not t2:
                self.isSame=False
                return
            
            if t1.val!=t2.val:
                self.isSame=False
                return
            
            bfs(t1.left,t2.left)
            bfs(t1.right,t2.right)
        
        bfs(p,q)
        return self.isSame

        