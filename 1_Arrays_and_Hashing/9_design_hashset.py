class ListNode:
    def __init__(self,val=None):
        self.val=val
        self.next=None
        self.prev=None

class MyHashSet:
    """
    Problem: 705. Design HashSet
    https://leetcode.com/problems/design-hashset/description/


    Intuition:
    - A proper solution requires understanding of collision handling: 
        - Open addressing [Chaining] (if collision occurs, store in a linked list at that position)
            - Make sure you insert in sorted order!
            - It uses extra space instead of available space
            - Load factor = numKeys/numSlots
        - Closed addressing (if collision occurs, go to next available index):
            - Usually end up having to resize if load factor >0.6-0.8
            - Linear probing (continue to probe next space)-> next idx to probe = (HashVal+i)%Buckets where i=probe number
            - Quadratic probing (probe next idx: HashVal + i^2 where i=number of times you have porbed)
                - Assume HashVal=0, you get collision, i becomes 1, you check idx=0+1=2
                - Assume another collision, i becomes 2, you check idx=0+2^2=4
            - Double Hashing (use another hash function when you get collision)
    
        The implementation would be cleaner if we used a dummy node as head (instead of using it as a tail, which doesnt exactly help us)
    """
    def __init__(self):
        self.hashSet=[ListNode() for _ in range(10**4)] #default of size 10**4 
        #DO NOT initialize self.hashMap=[ListNode()]*(10**4) -> this creates only one listnode and repeats its reference
        # this goes for all types that are referenced (for example lists)
        self.n=10**4

    def add(self, key: int) -> None:
        if self.contains(key):
            return

        hashVal=key%self.n
        curr=self.hashSet[hashVal]
        head=self.hashSet[hashVal]

        while curr.val is not None and curr.val<key: #checking for sorted order
            curr=curr.next
        #now either curr.val = None, or curr.val is greater than key
        temp=ListNode(key)
        temp.prev=curr.prev
        if temp.prev:
            temp.prev.next=temp
        temp.next=curr
        curr.prev=temp

        if curr==head:#curr was head (and we are inserting in its place), then we need to update head
            self.hashSet[hashVal]=temp

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        
        hashVal=key%self.n
        curr=self.hashSet[hashVal]
        head=self.hashSet[hashVal]

        while curr.val !=key: #safe because we know key exists
            curr=curr.next
        
        if curr.prev:
            curr.prev.next=curr.next
        curr.next.prev=curr.prev

        if curr==head: #if curr was head (and is being deleted now), update head
            self.hashSet[hashVal]=curr.next
        del curr
        
    def contains(self, key: int) -> bool:
        hashVal=key%self.n
        curr=self.hashSet[hashVal]

        while curr.val is not None and curr.val<=key:
            if curr.val==key:
                return True
            curr=curr.next
        return False



class MyHashSetNaive:
    """
    We just initialize the hashSet (i.e. the array storing true/false) to be of size 10**6+1 because range of values in 0<=n<=10**6
    """

    def __init__(self):
        self.hashSet=[False]*(10**6+1)  #at most this many insetions      

    def add(self, key: int) -> None:
        self.hashSet[key]=True

    def remove(self, key: int) -> None:
        self.hashSet[key]=False
        
    def contains(self, key: int) -> bool:
        return self.hashSet[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)