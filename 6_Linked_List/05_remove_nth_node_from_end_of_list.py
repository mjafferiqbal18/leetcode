# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Problem: 19. Remove Nth Node From End of List
        https://leetcode.com/problems/remove-nth-node-from-end-of-list/

        Intuition:
        - We first need to find the nth node, and track its prev node as well
        - You start moving the tracking pointers (prev,toremove) with a delay
        - If delay == n, then when original ptr reaches the LAST NODE, toremove would be at the right place
        - You will have to dry run it once to know if youre doing it correctly
        - Edge case:
            - toRemove could be head and prevToRemove could be None
            - prevToRemove is not None
        
        Time:
        - O(n)

        Space:
        - O(1)

        """
        end=head
        count=0
        to_remove=head
        prev_to_remove=None

        if end and not end.next and n==1:
            return None

        #identify the node that needs to be removed
        while end.next:
            end=end.next
            count+=1
            if count>=n: #you should only start moving prev,toremove with a 
                prev_to_remove=to_remove
                to_remove=to_remove.next
        
        #remove the node
        if prev_to_remove:
            prev_to_remove.next=to_remove.next
            to_remove.next=None
        elif to_remove==head:
            head=head.next

        return head
        

            