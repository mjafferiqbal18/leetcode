class MyStack:
    """
    Problem: 225. Implement Stack using Queues
    https://leetcode.com/problems/implement-stack-using-queues/

    Intuition:
        - We can only use standard queue operations (pushToBack, peekAtFront, removeFromFront, size, isempty)
        - We can use 2 queues, q1 to hold the latest pushed element and q2 to hold the rest of the elements
        - For Push:
            - When we push to q1, we take whatever's in q1 and push it to q2
        - For Pop:
            - When we pop from q1, we need to make sure q1 contains second most recent
            - To do that, we push everything from q1 into q2, and then everything except last element from q1 to q2
            - This ensures q1 now has the next most recent element, while q2 is the rest
        - For Top:
            - Return q1[0] since it contains the most recently added element
        - IsEmpty: 
            - pretty standard
        
        Time:
        - pop is O(n), rest is O(1)

        Space:
        - O(n)
    """
    def __init__(self):
        self.q1=deque()#stack
        self.q2=deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        if len(self.q1)>1:
            self.q2.append(self.q1.popleft())

    def pop(self) -> int:
        e=self.q1.popleft()
        while self.q2:
            self.q1.append(self.q2.popleft())
        while self.q1 and len(self.q1)!=1:
            self.q2.append(self.q1.popleft())
        
        return e

    def top(self) -> int:
        if self.q1:
            return self.q1[0]
        
    def empty(self) -> bool:
        return len(self.q1)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()