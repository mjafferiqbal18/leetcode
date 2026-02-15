# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Problem: 141. Linked List Cycle
        https://leetcode.com/problems/linked-list-cycle/

        Intuition:
        - You could either keep storing the nodes seen, or you could use a slow and a fast pointer
        - Using slow and fast ptr, Space O(1) and Time O(n)

        Alternative is to hash every seen node and check hashset -> Time O(n) but Space also O(n)
        """
        slow,fast=head,head
        while slow and fast: 
            slow=slow.next
            fast=fast.next
            if not fast: #fast reached the end without meeting slow (so there is an end, and hence no cycle)
                return False
            else:
                fast=fast.next
            if slow==fast: #becuase of a cycle, fast will eventually meet slow
                return True
        
        return False
            
        