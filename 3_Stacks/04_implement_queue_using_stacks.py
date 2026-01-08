class MyQueue:
    """
    Problem: 232. Implement Queue using Stacks
    https://leetcode.com/problems/implement-queue-using-stacks/

    Intuition:
    - We can only use standard queue operations (pushToBack, peekAtBack, removeFromBack, size, isempty)
    - We can use 2 stacks, s1 to hold the oldest pushed element and s2 to hold the rest of the elements
    - For Push:
            - only push to s1 if s1 empty, else push to s2
            - makes a natural ordering where s1 is oldest elem, s2 front has next and so on
        - For Pop:
            - When we pop from s1, we need to make sure q1 contains second oldest (which is at the start of s2)
            - We pop from s2 apart from the last element and hold that in s1
            - Then pop the last elem in s2 (that should go in s2), and hold it in a variable (temp)
            - Then pop everything again from s1 into s2
            - put temp back into s1
                - e.g. s1=[y], s2=[x,z,a], elem, temp
                       s1=[ ], s2=[x,z,a], elem=y, temp
                       s1=[a,z], s2=[x], elem=y, temp
                       s1=[a,z], s2=[ ], elem=y, temp=x
                       s1=[], s2=[z,a], elem=y, temp=x
                       s1=[x], s2=[z,a], elem=y
                        return elem
        - For Top:
            - Return s1[-1] since it contains the least recently added element
        - IsEmpty: 
            - pretty standard (size of s1)
    """

    def __init__(self):
        self.s1=[] #holds the top of the queue (element that was inserted first)
        self.s2=[]
        
    def push(self, x: int) -> None:
        if not self.s1:
            self.s1.append(x)
        else:
            self.s2.append(x)

    def pop(self) -> int:
        elem=self.s1.pop() #held the last element
        
        #now s1 is empty
        if not self.s2:
            return elem
        
        while len(self.s2)!=1:
            self.s1.append(self.s2.pop())
        
        temp=self.s2.pop()

        #now s2 is also empty
        while self.s1:
            self.s2.append(self.s1.pop())
        
        self.s1.append(temp) #now s1 has the next least recent elem
        return elem

    def peek(self) -> int:
        if self.s1:
            return self.s1[-1] #last inserted element into s1        

    def empty(self) -> bool:
        if not self.s1:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()