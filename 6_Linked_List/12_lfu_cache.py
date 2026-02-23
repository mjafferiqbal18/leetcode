class Node:
    def __init__(self,value=None):
        self.next = None
        self.prev = None
        self.val = value

class LFUCache:
    """
    Problem: 460. LFU Cache
    https://leetcode.com/problems/lfu-cache/

    Intuition:
    -  We have our regular cache which maps a key to value
        - We need to track usedCounts and also the nodes that correspond to a usedCount (alongside their order)
        -  lets say we map a usedCount -> keys that have this usedCount
            - We would need to preserver insert order (so cant use a hashmap because it doesnt order)
            - We would have to remove from this list (often from middle) -> we cant use a list, could use a linkedlist
        - To track usedCounts we can use a sortedSet (otherwise this operation would take O(counts), but that shouldnt be that much of a problem itself)
    - if we have usedCount -> linkedlist containing nodes (keys) which preserve LFU order
        - we can add / remove in O(1) time if doubly linked list
    - if we have active counts (sortedSet) we can update/remove active counts in O(logn), and access smallest active count in O(1)
    - We can also have a separate map for key -> usedCount

    - Implementing removeLeastFrequencyUsed:
        - you look at the smallest active count, go to the countToKey map's list, then remove the node from there
    
    - Implemnting get:
        - you increment the key's active count 
    
    - Implementing put:
        - case 1: new key
            you check cache size, and call removeLeastFrequencyUsed

        - case 2: old key
            - very similar to get
    
    """

    def __init__(self, capacity: int):
        self.cache = {} # maps a key to its (value,node)
        self.countToKeys = {} # maps a usedCount to a linked list stored as [left,right]
        self.keyToCount = {} # maps a key to its used count
        self.activeCounts = SortedSet() # stores the counts available
        self.cap = capacity
        self.n = 0
        
    def initializeLeftRight(self):
        left = Node()
        right = Node()
        left.next = right
        right.prev = left
        return [left,right]

    def removeLeastFrequentlyUsed(self): 
        """
            Least frequently used will be the node pointed to by right
        """
        if self.activeCounts: #if something is stored
            leastUsedCount = self.activeCounts[0] #this is the lowest count
            leftK, rightK = self.countToKeys[leastUsedCount] #this list represents keys with usedcount = leastUsedCount
            
            nodeToRemove = leftK.next #we guarantee that leftK.next != rightK
            leftK.next = nodeToRemove.next
            nodeToRemove.next.prev = leftK

            keyToRemove = nodeToRemove.val
            del self.cache[keyToRemove] 
            self.n -= 1

            if leftK.next == rightK: #no key has this count any more
                del self.countToKeys[leastUsedCount]
                self.activeCounts.remove(leastUsedCount)

            # print("Least Frequently Used Key:",keyToRemove)
            # print("#############")
                    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        val, node = self.cache[key]

        # update the count in keyToCount
        oldCount = self.keyToCount[key] 
        newCount = oldCount + 1 
        self.keyToCount[key] = newCount

        # add the count to active counts 
        self.activeCounts.add(newCount)

        # remove node from self.countToKeys[oldCount]
        node.prev.next = node.next
        node.next.prev = node.prev 

        # check if self.countToKeys[oldCount] has no other nodes available, if not, then remove from countToKeys and activeCounts
        left, right = self.countToKeys[oldCount]
        if left.next == right: # no node in between
            del self.countToKeys[oldCount]
            self.activeCounts.remove(oldCount)

        # insert node in self.countToKeys[newCount]
        if newCount not in self.countToKeys:
            self.countToKeys[newCount] = self.initializeLeftRight()
        left, right = self.countToKeys[newCount]
        previousNode = right.prev
        previousNode.next = node
        node.prev = previousNode
        node.next = right
        right.prev = node

        # print('Get | key:',key,", value:",val)
        # print("countToKeys Keys:",self.countToKeys.keys())
        # print("keyToCount:",self.keyToCount)
        # print("activeCounts:",self.activeCounts)
        # print('##########')

        return val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache: #this is a new key
            if self.n == self.cap: #we need to remove an elem
                self.removeLeastFrequentlyUsed()
            
            # add key to cache
            keyNode = Node(key)
            self.cache[key] = [value, keyNode]

            # add the count to keyToCount
            self.keyToCount[key] = 1

            # add the count to active counts
            self.activeCounts.add(1)

            # insert node in self.countToKeys[1]
            if 1 not in self.countToKeys:
                self.countToKeys[1] = self.initializeLeftRight()
            left, right = self.countToKeys[1]
            previousNode = right.prev
            previousNode.next = keyNode
            keyNode.prev = previousNode
            keyNode.next = right
            right.prev = keyNode

            # update current count
            self.n += 1

        else: # this is an old key
            oldVal, node = self.cache[key] 
            self.cache[key] = [value, node]

            # update the count in keyToCount
            oldCount = self.keyToCount[key] 
            newCount = oldCount + 1 
            self.keyToCount[key] = newCount

            # add the count to active counts 
            self.activeCounts.add(newCount)

            # remove node from self.countToKeys[oldCount]
            node.prev.next = node.next
            node.next.prev = node.prev 

            # check if self.countToKeys[oldCount] has no other nodes available, if not, then remove from countToKeys and activeCounts
            left, right = self.countToKeys[oldCount]
            if left.next == right: # no node in between
                del self.countToKeys[oldCount]
                self.activeCounts.remove(oldCount)

            # insert node in self.countToKeys[newCount]
            if newCount not in self.countToKeys:
                self.countToKeys[newCount] = self.initializeLeftRight()
            left, right = self.countToKeys[newCount]
            previousNode = right.prev
            previousNode.next = node
            node.prev = previousNode
            node.next = right
            right.prev = node
        
        # print('Put | key:',key,", value:",value)
        # print("countToKeys Keys:",self.countToKeys.keys())
        # print("keyToCount:",self.keyToCount)
        # print("activeCounts:",self.activeCounts)
        # print('##########')


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)