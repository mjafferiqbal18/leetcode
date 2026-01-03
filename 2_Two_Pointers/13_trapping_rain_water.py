class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Problem: 42. Trapping Rain Water
        https://leetcode.com/problems/trapping-rain-water/

        Intuition:
            - The easiest way to think about it is that at a cell, water= max(0, min(maxHeightL, maxHeightR)-height[i])
            - We use a prefixPostfix array to solve it
                - Time= O(n), Space= O(n)
            
            - To solve in O(1) space, we can use two pointers:
                - l=0, r=n-1: these are boundaries so they can store any water (it'll spill)
                - also have a maxL (max height to the left of ptr l) and maxR (max height to the right of ptr r)
                - we choose the smaller one to process (calculate water) and then shift it
                    - when processing it, we only use its (maxL if l, or maxR if r) as limiting wall
                    - Refer to logical explanation in the twoPointers() function
        """

        def prefixPostfix():
            n=len(height)
            prefix=[0]*n
            postfix=[0]*n

            maxL=0
            maxR=0

            #fill prefix and postfix
            for i in range(n):
                prefix[i] = maxL
                maxL = max(maxL, height[i])
                postfix[n-i-1] = maxR #postfix idx would be n-1-i since thats being filled from end to start
                maxR = max(maxR, height[n-i-1]) 

            res=0
            for i in range(n):
                # we need to make sure that we dont add negative numbers into res, so we take max with 0
                # min(prefix[i],postfix[i]) decides the amount of water, and we subtract height of current cell to calculate water on top of the cell
                res+= max(0, min(prefix[i],postfix[i])-height[i])
            return res
        # return prefixPostfix()
            

        def twoPointers():
            n=len(height)
            l=0
            r=n-1
            maxL=0
            maxR=0
            res=0

            while l<=r:
                if height[l]<=height[r]: #choose l to process
                    """
                    - we advance the ptr (left or right) whichever one is smaller
                    - say height[l]<=height[r]. that height[r] is >= height left, and maxR>=height[l]
                    - at height[l], the limiting factor is only maxL, so we use that
                    - the opposite logic is true for height[l]>height[r]
                    - Why (in height[l]<=height[r]) res += max(0, min(maxL,maxR) - height[l]) is wrong:
                        - because if at height[l], there could be a huge wall between l and r that you havent processed yet, and the current maxR might be small 
                            - (the actual wall causing water to be trapped at l could exist somewhere between l and r)
                            - doing min(minL,minR) will cause you to undercount
                    """
                    # we advance the ptr (left or right) which is 
                    res += max(0, maxL - height[l]) 
                    maxL = max(maxL, height[l])
                    l+=1
                else:
                    res += max(0, maxR - height[r])
                    maxR = max(maxR, height[r])
                    r-=1
            return res
        return twoPointers()


        """
        Time O(n)
        Space O(1)

        in this solution you start from l,r and fill water when u can, based on 
        the minimum of l and r
        then as you encounter more land you want to subtract some water taken up 
        by that land
        if you find a new minimum l,r then you add more water

        Neetcode's solution doesnt fill water at a level, but instead defines the equation:
        (maxL_height - maxR_height) - height[i] if >0 else 0
        So he ONLY adds water when he needs to -> 
        and in his O(1) sol, because you're shifting the minimum, you dont always need to know max lef and right
        you can make do with one of these, since we take the minimum of the two
         
        
        """
        l=0
        r=len(height)-1
        water=0
        Min=0
        moved=-1

        while l<r:
            if min(height[l],height[r])>Min:
                #subtract
                if water>0 and height[moved]!=0:
                    water-=min(Min,height[moved])

                oldMin=Min
                Min=min(height[l],height[r])    
                
                #add
                water+=((r-l-1)*(Min-oldMin)) #add units of area 

                #move the smaller height
                if height[l]<height[r]:
                    l+=1
                    moved=l
                elif height[l]>height[r]:
                    r-=1
                    moved=r
                else:
                    r-=1
                    moved=r

            else:
                #subtract
                if water>0 and height[moved]!=0:
                    water-=min(Min,height[moved])
                
                #move the smaller height
                if height[l]<height[r]:
                    l+=1
                    moved=l
                elif height[l]>height[r]:
                    r-=1
                    moved=r
                else:
                    l+=1
                    moved=l
        return water
    
    

   