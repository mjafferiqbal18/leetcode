# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Problem: 23. Merge k Sorted Lists
        https://leetcode.com/problems/merge-k-sorted-lists/

        Intuition:
        - You have k lists, if you need to merge them, youd need to find the smallest of them
            - this can be done with a minHeap in logk
        - We can do this inplace
            - First initialize the list using a dummy node to track, then we can do merging in place

        Time:
        - O(logk)

        Space:
        - O(n)
        """
        minHeap=[]
        n=len(lists)
        for i in range(n):
            if lists[i]: #captures the head, if it is not null 
                heapq.heappush(minHeap,(lists[i].val,i)) # push (value,i)
        
        #initialize new list
        dummy=ListNode(-1,None)
        tail=dummy

        while minHeap: #all nodes will eventually make their way into the heap
            value,idx=heapq.heappop(minHeap) #smallest value, idx
            
            #inplace
            tail.next=lists[idx]
            tail=tail.next
            lists[idx]=lists[idx].next
            if lists[idx]: #if the node is not null
                heapq.heappush(minHeap,(lists[idx].val,idx)) #add to heap
        return dummy.next

        