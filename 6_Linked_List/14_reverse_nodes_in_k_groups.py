# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """   
        Problem: 25. Reverse Nodes in k-Group
        https://leetcode.com/problems/reverse-nodes-in-k-group/

        Intuition:
        - You track the count of nodes seen, once that reaches k, you reverse the last k nodes seen
            - You reverse it such that it becomes in fragments (i.e. you initialize prev = None)
        - Then you also make sure to record the st and end of the fragment
        - At the end, you stitch the fragments together
            - Make sure to handle the edge case (example 1, node 5) where num nodes % k != 0
        
        Time:
        - O(n)

        Space:
        - O(1)

        """
        nodeCount=0 #denotes number of nodes visited
        dummyNode=ListNode(-1,None) 
        temp=head #tracks the curr node

        #pointers initialized at the start of this list to reverse
        curr=head
        prev=None

        #we will use these to stitch the fragments totgether
        fragments=[]

        while temp: 
            temp = temp.next 
            nodeCount += 1 #we have seen one node

            if nodeCount==k: #once we have seen k nodes, we need to reverse them. temp is at the node after the kth node
                listEnd=curr #the start of the list will become the end after reversal
                while curr and curr!=temp: #we continue until we exhaust k nodes
                    tempStore=curr.next 
                    curr.next=prev 
                    prev=curr
                    curr=tempStore
                listStart=prev #the prev at the end becomes the start

                fragments.append([listStart,listEnd]) #we append the start and end of the list
                tempRestart=temp  #this records the start of the last list (which is helpful to track cause it may not make it to fragments - see the 5th node in example 1)
                # temp would be null if total number of nodes is divisible by k
                prev=None
                nodeCount=0 #we reset the node count as well

        # print the fragments for logging
        # for f in fragments:
        #     ls='None' if f[0] is None else f[0].val
        #     le='None' if f[1] is None else f[1].val
        #     print('listStart:',ls,'listEnd:',le)
        # print(temp.val)

        numFragments=len(fragments)
        endOfPrevFrag=None
        for i in range(numFragments):
            if i==0:
                head=fragments[i][0]
                endOfPrevFrag=fragments[i][1]
            else:
                if endOfPrevFrag:
                    endOfPrevFrag.next=fragments[i][0]
                    endOfPrevFrag=fragments[i][1]

        fragments[-1][1].next=tempRestart 
        return head