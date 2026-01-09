class MinStack:
    """
    Problem: 155. Min Stack
    https://leetcode.com/problems/min-stack/

    Intuition:
    - We need a regular stack to store all elems
    - We can use a monotonically decreasing stack to store minimums -> getMin would be constant time
    - When popping, you check if the elem you're popping is minTop too, if yes then also pop from minStack

    Time:
    - O(n)

    Space:
    - O(n)
    """

    def __init__(self):
        self.stack=[]
        self.topStack=-1
        self.minStack=[]
        self.minTop=-1
        self.count=0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.topStack+=1
        self.count+=1

        if self.minTop==-1: #is empty
            self.minStack.append(val)
            self.minTop+=1
        else:#look at top
            if val<=self.minStack[self.minTop]:
                self.minStack.append(val)
                self.minTop+=1

    def pop(self) -> None:
        self.topStack-=1

        if self.stack[self.topStack+1]==self.minStack[self.minTop]:
            del self.minStack[-1]
            self.minTop-=1

        del self.stack[-1] #you could alternatively do self.minStack.pop()
    

    def top(self) -> int:
        return self.stack[self.topStack]

    def getMin(self) -> int:
        return self.minStack[self.minTop]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()