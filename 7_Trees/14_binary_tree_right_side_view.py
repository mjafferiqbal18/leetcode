# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Problem: 199. Binary Tree Right Side View
        https://leetcode.com/problems/binary-tree-right-side-view/

        Do bfs (with queue) and only store the last element of the level in res
        Since we are doing bfs from left to right, this should work

        Time:
        - O(n)

        Space:
        - O(n)
        """
        res=[]
        que=collections.deque()
        que.append(root)
        while que:
            level=[]
            len_q=len(que)
            for i in range(len_q):
                node=que.popleft()
                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if level:
                res.append(level[-1]) #only store the last elem
        return res

        