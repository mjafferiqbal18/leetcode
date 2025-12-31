class ListNode:
    def __init__(self,key=None,val=None):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
    
class MyHashMap:
    """
    Problem: 706. Design HashMap
    https://leetcode.com/problems/design-hashmap/description/

    Same solution as Leetcode 705: Design HashSet
    We will use a smaller map size to demonstrate collisions and use open addressing to address them
    Same argument of keeping the linked lists in sorted order to cut down on search time
    Linkedlist node will have another attribute for storing value to the key
    """
    def __init__(self):
        self.hashMap=[ListNode() for _ in range(10**4)]
        #DO NOT initialize self.hashMap=[ListNode()]*(10**4) -> this creates only one listnode and repeats its reference
        # this goes for all types that are referenced (for example lists)
        self.n=10**4

    def put(self, key: int, value: int) -> None:
        curr=self.contains(key)
        if curr is not None:
            curr.val=value
            return
        
        #key does not exist 
        hashVal = key%self.n
        curr = self.hashMap[hashVal]
        head= self.hashMap[hashVal]
        while curr.key is not None and curr.key<key:
            curr=curr.next
        
        #curr is either at end (curr.key==None) or at a key greater than key
        temp=ListNode(key,value)

        if curr==head:
            temp.next=curr
            curr.prev=temp
            self.hashMap[hashVal]=temp
        else:
            temp.next=curr
            temp.prev=curr.prev
            temp.prev.next=temp
            curr.prev=temp

    def get(self, key: int) -> int:
        curr=self.contains(key)
        if curr is None:
            return -1
        else:
            return curr.val

    def remove(self, key: int) -> None:
        curr=self.contains(key)
        if curr is None:
            return

        hashVal=key%self.n
        head=self.hashMap[hashVal]
        if curr==head:
            self.hashMap[hashVal]=curr.next
            curr.next.prev=None
        else:
            curr.prev.next=curr.next
            curr.next.prev=curr.prev
        del curr
        
    def contains(self,key:int) -> Optional[ListNode]:
        hashVal=key%self.n
        curr=self.hashMap[hashVal]

        while curr.key is not None and curr.key<=key:
            if curr.key==key:
                return curr
            curr=curr.next
        return None

class MyHashMapNaive:
    """
    Same solution as Leetcode 705: Design HashSet
    """
    def __init__(self):
        self.hashMap=[-1]*(10**6+1)

    def put(self, key: int, value: int) -> None:
        self.hashMap[key]=value

    def get(self, key: int) -> int:
        return self.hashMap[key]

    def remove(self, key: int) -> None:
        self.hashMap[key]=-1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)