class Solution:
    def isValid(self, s: str) -> bool:
        """
        Problem: 20. Valid Parentheses
        https://leetcode.com/problems/valid-parentheses/

        Intuition:
            - Either we open a parenthesis or we close one: 
                - When we close, the closing one HAS to match the most recently opened one
            - Very stacky problem: Keep pushing as long as we open, to close, try and match to the latest opened
                - if unmatched, then return False
            - Finally, stack needs to be empty (for it to be a valid sol) because once we close a set of brackets, we remove the open part from stack
                - '((((' wont raise alarms in the initial loop, but is not a valid parenthesis because stack is not empty
            
        Time: O(n)
        Space: O(n)
        
        """
        stack=[]
        closeToOpen={'}':'{',')':'(',']':'['}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else: #parenthesis dont match
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
            
        