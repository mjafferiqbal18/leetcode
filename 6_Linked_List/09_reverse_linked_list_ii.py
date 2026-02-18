# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Problem: 92. Reverse Linked List II
        https://leetcode.com/problems/reverse-linked-list-ii/

        Intuition:
        - You need to track start and end of the list; once you can find that then you imagine breaking the list up (before,listToBeReversed,after)
        - Just iterate over the list to find the st, node before st, end, node after end
        - reverse from st to end
        - nodeBeforeSt.next = end, st.next = nodeAfterEnd

        Time:
        - O(n)

        Space:
        - O(1)

        """
        if left==right: #no reversal needed
            return head

        temp=head
        prevl,l=None,head
        nextr,r=head,head
        count=1

        while temp.next: 
            count+=1 #keeps track of the position
            if count==left: #we have reached the start of the list
                prevl=temp #grab the node previous to it
                l=temp.next #grab left itself
            elif count==right:
                r=temp.next #we have reached the end of the list
                nextr= temp.next.next #grab the node after it
            temp=temp.next 
        
        if prevl: #which means that l is not head
            prevl.next=r

        p,temp=None,l #remember, to reverse a linkedlist, you initialize temp at 'head'(or st in this case), and prev to None

        while temp and temp!=nextr:
            t=temp.next
            temp.next=p
            p=temp
            temp=t
        
        if l: #l is now at end
            l.next=nextr
        
        if not prevl: #if initially l was head, then prevl was None, in which case head becomes r
            head=r
        return head
        