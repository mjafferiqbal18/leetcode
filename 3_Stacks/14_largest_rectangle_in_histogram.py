class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Problem: 84. Largest Rectangle in Histogram
        https://leetcode.com/problems/largest-rectangle-in-histogram/

        Intuition:
        - A histogram of a certain height can extend as long as you dont encounter a height less than you
        - Once you do, that height can extend left as long as it sees heights <= it
        - Rest is just implementation detail

        Time:
        - O(n)

        Space:
        - O(n)


        You append to stack (my height,idx) if empty
        if currheight< whatevers in the stack, you start popping (until stack top <= to you), and calculating area 
        if currheight is == to stack top, you move on
        if currheight is > stack top, you add yourself to the stack and move on

        at the end, you go over the stack (because some values havent been popped) you pop and compute areas
        if a value exists in the stack, that mean no value was smaller than this one from its idx to the end

        """
        i=0
        n=len(heights)
        stack=[]
        len_stack=0
        maxArea=max(heights)

        for i in range(n):
            if stack:
                if stack[-1][0]<heights[i]:  #if stack top is less that you
                    stack.append((heights[i],i)) #push yourself, move forward
                elif stack[-1][0]>heights[i]:   #if stack top is greater
                    finalIdx=i
                    while stack and stack[-1][0]>heights[i]: 
                        hPrime,hPrimeIdx=stack.pop() #
                        maxArea=max(maxArea,hPrime*(i-hPrimeIdx))
                        finalIdx=hPrimeIdx

                    if not(stack and stack[-1][0]==heights[i]):
                        stack.append((heights[i],finalIdx))
                #we do nothing if equal
            else:
                stack.append((heights[i],i))

        len_stack=len(stack)
        for i in range(len_stack):
            hPrime,hPrimeIdx=stack.pop()
            maxArea=max(maxArea,((n-1)-hPrimeIdx+1)*hPrime)
        return maxArea

