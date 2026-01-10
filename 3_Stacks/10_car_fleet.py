class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Problem: 853. Car Fleet
        https://leetcode.com/problems/car-fleet/

        Intuition:
        - First, we can sort based on position in ascending order. 
        - Then we find their corresponding times based on position and speed: time=(target-pos)/speed
        - Then iterating from the end:
            - if time[i]<=time[i+1] -> then it has to be absorbed by car at pos[i+1] because car pos[i] cant cross the car at pos[i+1]
            - since we are 'resolving' cases by grouping them we could use a stack here, but we dont really need to
        
        Time = (nlogn+n) = O(nlogn) because of sorting
        Space = O(n) -> can be O(1)
        NOTE: helpful to know how to zip and then sort based on a specific element

        You could also just skip the stack and use constant memory (one variable to keep track of next time) and also to keep track of fleets
        """
        posSpeed=sorted(zip(position,speed))  #sorted by position
        stack=[]
        # n=len(position)
        for i in range(len(position)-1,-1,-1):
            time=(target-posSpeed[i][0])/posSpeed[i][1]
            if stack:
                if time>stack[-1]:
                    stack.append(time)
            else:
                stack.append(time) 
        return len(stack)
        
    def carFleet2(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Using a forward pass
        """
        posSpeed=sorted(zip(position,speed), key=lambda x:x[0])  #sorted by position
        stack=[]
        fleet=len(position)
        for pos_speed in posSpeed:
            time=(target-pos_speed[0])/pos_speed[1]
            while stack and time>=stack[-1]: #basically ensures all stuff smaller than you in stack now become a fleet with you
                stack.pop()
                fleet-=1
            stack.append(time)
        return fleet

    


