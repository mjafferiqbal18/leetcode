class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Problem: 735. Asteroid Collision
        https://leetcode.com/problems/asteroid-collision/

        Intuition:
        - Recognize that we can use stack since we have to explode (and thus remove) asteroids, and then also add them back
        - We'll have to add negs to the stack too since we need to return the final state of the stack
        - Just pop the last two elems if secondlast is rightGoing and last is leftGoing
            - Use a while loop for this since the leftGoing could be really big and could continue to destroy rocks
            - After the while loop ends, we can be sure that there are no leftGoing asteroids at a higher idx than rightGoing asteroids
        
        Time:
        - O(n)

        Space:

        
        """
        stack=[]
        n=len(asteroids)

        for i in range(n):
            stack.append(asteroids[i]) #add this to the stack
            #you can only perform a destructive opp if >=2 elems remain
            #secondLast has to be positive (right going) and last has to be negative (left going)
            while len(stack)>=2 and stack[-1]<0 and stack[-2]>0: 
                left=stack.pop()
                right=stack.pop()
                if right>abs(left): #right survives
                    stack.append(right)
                elif abs(left)>right: #left survives
                    stack.append(left)
        return stack
        