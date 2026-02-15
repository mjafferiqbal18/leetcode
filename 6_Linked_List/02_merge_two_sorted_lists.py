# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem: 21. Merge Two Sorted Lists
        https://leetcode.com/problems/merge-two-sorted-lists/

        Intuition:
        - USE A DUMMY node to track the final list (you only need to re-route pointers, and NOT initialize new one)
            - start building the list from the dummy, so that head would be dummy.next
            - Start at both lists, and append to your new list (without making new nodes) based on whatever is smaller
        - Use a dummy node to avoid edge cases for initial empty list

        Time:
        - O(n)

        Space:
        - O(1)

        """
        dummy=ListNode()
        tail=dummy 

        while list1 and list2:
            if list1.val<=list2.val:
                tail.next=list1 
                list1=list1.next #advance list 1
            else:
                tail.next=list2 
                list2=list2.next #advance list 2
            tail=tail.next #advance the merged list
        
        #if one list empty and the other remains, insert that as well
        if list1:
            tail.next=list1
        elif list2:
            tail.next=list2
        return dummy.next
            
        

        