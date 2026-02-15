# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem: 206. Reverse Linked List
        https://leetcode.com/problems/reverse-linked-list/

        Intuition:
        - start prev at null, and curr at head
        - make curr.next=prev, and shift both prev and curr forward (you have to use a temp variable)
        - your head will be prev at the end of the linked list, and curr will be None

        Time: 
        - O(n)

        Space:
        - O(1)
        """
        prev,curr=None,head
        while curr:
            temp=curr.next #temporarily store whats in curr.next
            curr.next=prev #set current node's next to previous
            prev=curr #shift prev forward
            curr=temp #shift curr forward
        return prev