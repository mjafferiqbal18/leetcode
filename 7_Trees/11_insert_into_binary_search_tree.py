# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Problem 701. Insert into a Binary Search Tree
        https://leetcode.com/problems/insert-into-a-binary-search-tree/

        Intuition:
        - This is not an avl tree, so it can be unbalanced
        - To be a binary search tree, everything to your left has to be smaller than you, and everything to your right has to be larger than you
        - We can just keep traversing the tree until we hit a leaf
            - At that point we make a node for val and set the prevNode to point at us (we will have to track left/right)
        - You also need to do an early termination check at the start:
            - if root is null, then return TreeNode(val)

        Time:
        - O(logn)

        Space:
        - O(1)

        """
        if not root:
            return TreeNode(val)

        curr = root
        prev = None
        prevDir = None
        while curr:
            if val > curr.val: #go right
                prev = curr
                prevDir = 'r'
                curr = curr.right
            elif val < curr.val: #go left
                prev = curr
                prevDir = 'l'
                curr = curr.left
        
        newNode = TreeNode(val)
        if prevDir == 'r':
            prev.right = newNode
        elif prevDir == 'l': 
            prev.left = newNode
        
        return root
        
                
        