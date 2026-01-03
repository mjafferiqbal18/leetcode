class Solution:
    """
    Problem: 682. Baseball Game
    https://leetcode.com/problems/baseball-game/

    Intuition:
        - We can assume operations are going to be in proper order (i.e. we should get a score initially)
        - At each opp, we grab the latest score(s), do something, and store the result as the latest score
        - We grab latest, change it, update latest val
        - This screams stack -> grab the value that has been appended recently
        - Note: we only remove latest (pop from stack) at opp=='C', otherwise we keep old scores since we need to use them
    
    Time=O(n)
    Space= O(n)

    """
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for opp in operations:
            if opp=='+':
                stack.append(stack[-1]+stack[-2])
            elif opp=='D':
                stack.append(2*stack[-1])     
            elif opp=='C':
                stack.pop()
            else:
                stack.append(int(opp))
        return sum(stack)  