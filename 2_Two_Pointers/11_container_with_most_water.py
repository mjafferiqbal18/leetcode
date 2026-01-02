class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Problem: 11. Container With Most Water
        https://leetcode.com/problems/container-with-most-water/

        Intuition:
            - You use two pointers at far ends (use r-l+1 as width, height is the limiting factor)
            - When moving inwards you're decreasing width, so your best best is to move the limiting factor (in hopes for a higher value)
            - keep updating the max area seen
        
        Time:
        - O(n)

        Space:
        - O(1)
        """

        l=0
        r=len(height)-1
        area=0
        while l<r:
            limitingFactor=min(height[l],height[r])
            if limitingFactor*(r-l) > area:
                area=limitingFactor*(r-l)
            
            #update pointers, based on whichever is the limiting factor
            if height[l]<height[r]:
                l+=1
            elif height[r]<height[l]:
                r-=1
            else: #both equal, choose whichever leads to bigger height -> we can just choose any and it will lead us to the correct solution
                r-=1
        return area
