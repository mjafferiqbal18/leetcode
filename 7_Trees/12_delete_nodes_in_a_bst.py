# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Problem: 450. Delete Node in a BST
        https://leetcode.com/problems/delete-node-in-a-bst/

        Intuition:
        - It gets extemely messy if you do pointer gymnastics, so it is best to think of it in the sense of swapping values and deleting a leaf
        - You start with basic checks:
            - base case: if root none, return none
            - if val < root.val:
                - recursively call on left, return root
                - Remember: if val not found, you'll eventually let the tree be unchanged (and that is what we want)
            - if val > root.val:
                - recursively call on right, return root
            
        - if none of these hit, then you are at root, with key = root.val
        - There are 3 further cases:
            - root has no left 
            - root has no right
            - root has both children (this is the complex case)
                - you find the successor: left most node in the right subtree (it will max have a right subtree, nothing on left)
                - once successor is found, swap its value with the root
                - delete the successor by recursively calling on (right subtree, succ.val)

        Time:
        - O(logn)

        Space:
        - O(1)
        """

        if not root: # Base case: empty subtree -> we have nothing to delete
            return None

        if key < root.val: # If key is smaller, the node (if it exists) must be in the left subtree
            root.left = self.deleteNode(root.left, key) #recursively call function on left subtree
            return root

        if key > root.val: # If key is larger, the node (if it exists) must be in the right subtree
            root.right = self.deleteNode(root.right, key) #recursively call function on right subtree
            return root

        # ---- If we reach here, root.val == key: we have to delete root ----

        # Case 1: node has no left child
        # Then we can replace this node with its right child (could be None)
        if not root.left:
            return root.right

        # Case 2: node has no right child
        # Then we can replace this node with its left child
        if not root.right:
            return root.left

        # Case 3: node has TWO children
        # Standard trick:
        #   - Find the inorder successor (smallest value in the right subtree)
        #   - Copy successor's value into this node
        #   - Delete the successor node from the right subtree
        #
        # Why this works:
        #   - Successor is the next bigger value after root.val
        #   - Successor is guaranteed to have NO left child (because it's the leftmost)
        #   - So deleting the successor is easy (it has at most 1 child)

        # Find inorder successor: leftmost node in the right subtree
        succ = root.right
        while succ.left:
            succ = succ.left

        # Copy successor's value into current node
        root.val = succ.val

        # Now delete the successor value from the right subtree
        # (this removes the duplicate we just created)
        root.right = self.deleteNode(root.right, succ.val) #very clean way to remove the succ

        # Return the (possibly updated) root pointer
        return root