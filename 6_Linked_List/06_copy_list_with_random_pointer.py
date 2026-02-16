"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    Problem: 138. Copy List with Random Pointer
    https://leetcode.com/problems/copy-list-with-random-pointer/

    Intuition:
    - In one pass, we can make new normal nodes (without random pointer, because a node could point to a node up ahead that we havent seen)
    - In that pass, also map oldNode -> newNode in a hashmap
    - In second pass, update the random pointers of the newNode, by setting it to map[whatever was in random of old node] -> tells us new node to point to

    Time:
    - O(n)

    Space:
    - O(1)
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #pass 1:
        dummy=Node(-1,None,-1)
        newhead=dummy
        st=head

        new_idx_to_node={}
        old_node_to_idx={} #or you could just hash old node to the new node
        idx=0
        while st:
            dummy.next = Node(st.val,None,None) #make a new node
            new_idx_to_node[idx]=dummy.next #
            old_node_to_idx[st]=idx
            st=st.next
            dummy=dummy.next
            idx+=1

        newhead=newhead.next
        st_old=head
        st_new=newhead
        
        while st_old and st_new:
            #handle case of None/Null ptr above
            temp_old = st_old.random
            if temp_old:
                st_new.random=new_idx_to_node[old_node_to_idx[temp_old]]
            else:
                st_new.random=temp_old
            st_old=st_old.next
            st_new=st_new.next
        
        return newhead


        