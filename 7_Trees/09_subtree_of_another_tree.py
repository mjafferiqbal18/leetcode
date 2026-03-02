# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Problem: 572. Subtree of Another Tree
    https://leetcode.com/problems/subtree-of-another-tree/

    Intuition:
    - if subRoot is none, it is definitely a subtree of root
    - if subRoot is not none, yet root is none, then subRoot is not a subtree
    - else you call sameTree on that root, if true, then return
        - if not true, call recursively on left and right subtree and return OR of result
    
    Time:
    - O(n^2)

    Space:
    - O(1)


    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: #if subroot None, then it subtree of root, regardless of if root is nill or not
            return True
        if subRoot and not root:
            return False
        if self.sameTree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    
    def sameTree(self,t1,t2):
        if not t1 and not t2:
            return True
        if t1 and t2 and t1.val==t2.val:
            return self.sameTree(t1.left, t2.left) and self.sameTree(t1.right,t2.right)
        return False
        