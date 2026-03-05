# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Problem: 235. Lowest Common Ancestor of a Binary Search Tree
        https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


        Naive approach: Time: O(logn) Space:O(n)
            - search p, record ancestors in a set
            - search for q, and update min if ancestor in set
        
        Optimal approach: Time: O(logn) Space: O(1)
            - Recognize that the node at which split occurs, we have found the min ancestor
            - Node at which we split is last common ancestor, and also the l
        """

        curr=root
        while curr:
            if p.val>curr.val and q.val>curr.val:
                curr=curr.right
            elif p.val<curr.val and q.val<curr.val:
                curr=curr.left
            else: # but how is this the lca if p=7 and q=9
                return curr

        