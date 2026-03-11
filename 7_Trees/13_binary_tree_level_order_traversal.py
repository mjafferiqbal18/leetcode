# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    """
    Problem: 102. Binary Tree Level Order Traversal
    https://leetcode.com/problems/binary-tree-level-order-traversal/

    Intuition:
    - You use a queue to do the level order traversal
    - add root, and start loop until que not empty, also keep track of level
        - take len(queue), and pop that many times (these are nodes in current level)
        - when you pop, make sure to add any children to the queue
    
    Time:
    - O(n)

    Space:
    - O(n)
    
    
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que=collections.deque()
        que.append(root)
        res=[]
        while que:
            level=[]
            len_q=len(que) #this is done to separate levels
            for i in range(len_q):
                node=que.popleft()
                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if level:
                res.append(level)
        return res
            


        