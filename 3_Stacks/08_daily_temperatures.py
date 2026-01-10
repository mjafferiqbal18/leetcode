class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Problem: 739. Daily Temperatures
        https://leetcode.com/problems/daily-temperatures/

        Intuition:
        - In brute force, starting at a number you iterate ahead to find something bigger
            e.g. at 75, you iterate ahead until 76; at at 71 you iterate ahead till 72
            But iterating ahead from 71 to 72. is wasteful since we already see 72 while iterating from 75 to 76
            Need a way to tell future numbers that 'hey, i am unresolved'
            Very similar senario to valid parenthesis 'hey i am not closed yet'

        - We can use a monotonically decreasing stack to represent unresolved cases
            stack represents 'unresolved cases' (number for which a greater num has not been seen yet)
            you want to resolve the most recent unresolved case first (hence the stack) and stop when you cant
            Current number checks the stack and tries resolving as many as it can, then puts itself on the unresolved stack (in hopes a future number can resolve it)
        
        - Stack is applicable here because once you see a number that can resolve the top of the stack, it can continue to resolve more as long as top of stack is less than curr

        Time:
        - O(n)

        Space:
        - O(n)
        
        """
        if len(temperatures)<2: #early termination
            return [0]

        res=[0]*len(temperatures)
        stack=[]
        
        for idx,temp in enumerate(temperatures):
            if stack:
                while stack and temp > stack[-1][0]:
                    (smallT,smallIdx)=stack.pop() 
                    res[smallIdx]=idx-smallIdx
                stack.append((temp,idx))
            else:
                stack.append((temp,idx))
        return res

            
        