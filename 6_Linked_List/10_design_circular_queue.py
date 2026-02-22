class MyCircularQueue:
    """
    Problem: 622. Design Circular Queue
    https://leetcode.com/problems/design-circular-queue/

    Intuition:
    - Very easy to represent the queue with size = k, then use 2 ptrs to track the start and end and handle them accordingly
    - Didnt need to use a linked list because:
        - the queue is continuous, we dont need to remove elements from between the queue (for which we would need to shift the array around)

    Time:
    - O(n)

    Space:
    - O(k)
    
    """

    def __init__(self, k: int):
        self.q = [-1]*k
        self.l = 0
        self.r = 0
        self.n = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.n < self.k: #self.r must point to the next free idx
            self.q[self.r] = value
            self.n +=1
            self.updateR()
            return True
        else:
            return False
    
    def deQueue(self) -> bool:
        if self.n>0: #l must point to an idx that is filled and represents start of queue
            self.q[self.l] = -1
            self.n -= 1

            if self.n == 0:
                self.l,self.r = 0,0
            else:
                self.updateL()
            return True
        else:
            return False
        

    def Front(self) -> int:
        return self.q[self.l]

    def Rear(self) -> int:
        if self.q[self.r] != -1: #self.r is at full cap
            return self.q[self.r]
        else:
            i = (self.r-1 if self.r>0 else self.k-1)
            return self.q[i]

    def isEmpty(self) -> bool:
        return self.n == 0

    def isFull(self) -> bool:
        return self.n == self.k
    
    def updateR(self):
        """
        right should point at the next free idx to fill (or that last possible index that is currently filled)
        self. r can be to the right of self.l or to the left
        """
        self.r += 1
        if self.r == self.k: #we are out of bounds
            self.r = (0 if self.l !=0 else self.r-1)
        elif self.r == self.l: #we were to the left of self.l
            self.r -=1
    
    def updateL(self):
        """
        self.n is still > 0
        """
        self.l += 1 #increment l
        if self.l == self.k: #we are out of bounds
            self.l = 0 #we assume that if we were at n-1, then the next filled idx has to be at 0
        
        if self.q[self.r]!=-1: #if self.r did not point to a free idx (because there were no free spots), then just update it
            self.updateR()


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()