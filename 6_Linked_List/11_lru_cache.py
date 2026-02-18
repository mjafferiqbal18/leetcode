class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key=key
        self.val=val
        self.next=next
        self.prev=prev

class LRUCache:
    """
    Problem: 146. LRU Cache
    https://leetcode.com/problems/lru-cache/

    Intuition:
    Imagine the pairs, ordered and then imagine you need to make a node go to the front (because it was recently accessed)
    If we are doing this with a list, that means removing from curr pos and taking to end is O(n)
    This immediately means we need to use a linked list, and the linked list preserves the order
    If we get or put something, we remove it from list (if it exists) and put it to end of list
    When evicting, we remove the one pointed to by the head
    To get a key in O(1) we use a hashmap, where value is node (so we dont have to find in O(n))
    We can use a doubly linked list to do this, and use 2 dummy nodes (left and right) to track the list

    Time:
    - O(1) for remove, insert, get, put

    Space:
    - O(n) 

    """
    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={} #map key to ListNode
        self.left=ListNode()
        self.right=ListNode()
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self, node:ListNode):
        prev,nxt= node.prev, node.next
        prev.next=nxt
        nxt.prev=prev
    
    def insert(self, node:ListNode):
        #insert node before right ptr node
        self.right.prev.next=node
        node.prev=self.right.prev
        node.next=self.right
        self.right.prev=node

    def get(self, key: int):
        if key in self.cache:
            #remove node
            self.remove(self.cache[key]) #O(1)
            #insert node 
            self.insert(self.cache[key]) #O(1)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=ListNode(key,value,None,None)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            # self.cache.pop(lru.key)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)