# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Problem: 143. Reorder List
        https://leetcode.com/problems/reorder-list/

        Intuition:
        - We separate the two lists, reverse the second one, then merge both
        - NOTE: important to know how to find midpoint!!!

        Do not return anything, modify head in-place instead.
        """ 
        #find midpoint (basically want fast to go to the end, slow will be at midpoint)
        slow,fast=head,head
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        #2nd half starts at slow
        #reverse half
        prev,curr=None,slow.next
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        end=prev
        slow.next=None #at this point we have split the 2 linked lists

        #now we merge everything into l1
        l1,l2=head,end
        while l1 and l2:
            temp1=l1.next
            temp2=l2.next
            l1.next=l2
            l2.next=temp1
            l1=temp1
            l2=temp2

        
        


       