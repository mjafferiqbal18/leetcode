# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem: 2. Add Two Numbers
        https://leetcode.com/problems/add-two-numbers/

        Intuition:
        - The linked list already represents numbers from right to left, so that is convenient
        - Just use a carry, and iterate until one of the list becomes null
            - alternatively, you iterate until both are null, but handle cases where one is null by simulating padding (i.e. adding 0 to elem of the non null list)
        - Then you iterate over the other list (and add the carry to it)
        - Also handle the final carry at the end

        Time:
        - O(max(l1,l2))

        Space:
        - O(max(l1,l2))
        
        """
        carry=0
        dummy=ListNode(-1,None)
        head=dummy

        while l1 or l2:
            tempSum=0
            if l1 and l2: #if both exist, add the values and advance both
                tempSum=l1.val+l2.val
                l1=l1.next
                l2=l2.next 
            elif l1: # if only l1 exists, keep l1.val as tempSum, and advance l1
                tempSum=l1.val
                l1=l1.next
            elif l2:  # if only l2 exists, keep l2.val as tempSum, and advance l2
                tempSum=l2.val
                l2=l2.next
            tempSum=tempSum+carry # add the carry
            carry=0 #reset the carry

            if tempSum>=10: #if sum>10, then update sum and carry
                carry=tempSum//10
                tempSum=tempSum%10
            
            head.next=ListNode(tempSum,None) #set the value of new list to this sum
            head=head.next #advance the ptr 
        
        #assuming if both lists of same length, we might have an unhandled carry
        if carry>0: # handle the final carry
            head.next=ListNode(carry,None)
        
        return dummy.next





        