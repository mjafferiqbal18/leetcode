class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Problem: 85. Maximal Rectangle
        https://leetcode.com/problems/maximal-rectangle/

        Intuition:
        - Make a 2d prefix array (from top to bottom), that allows us to visualize histograms row by row
        - Then run (84. Largest Rectangle in Histogram) for each row

        Time:
        - O(n*m)

        Space:
        - O(n*m)

        Couldnt do myself, had to watch strivers video

        Could use the largest rectangle in histogram solution
        """
        prefixArr=self.makePrefixArr(matrix)
        n=len(prefixArr[0])
        maxH=0
        for row in prefixArr:
            maxH=max(maxH,self.largestRectangeInHistogram(row,n))
        return maxH
        
    
    def largestRectangeInHistogram(self,heights,n):
        stack=[(heights[0],0,0)] #height,st,end
        maxH=max(heights)
        for i in range(1,n):
            leftMostIdxICanStretchTo=i
            rightMostIdxElemCanStretchTo=i-1
            while stack and stack[-1][0]>=heights[i]:
                h,l,r= stack.pop()
                maxH=max(maxH,h*(r-l+1))
                maxH=max(maxH,h*(rightMostIdxElemCanStretchTo-l+1))
                leftMostIdxICanStretchTo=l
            stack.append((heights[i],leftMostIdxICanStretchTo,i))
        
        #we should have an increasing stack at the end 
        for elem in stack:
            h,l,r= elem[0],elem[1],elem[2]
            maxH = max(maxH, h*((n-1)-l+1))
        return maxH
    
    def makePrefixArr(self,matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        prefixArr = [[0]*cols for _ in range(rows)]
        
        for c in range(cols):
            prefixArr[0][c]=int(matrix[0][c])
        
        for r in range(1,rows):
            for c in range(cols):
                if matrix[r][c]!='0':
                    prefixArr[r][c]=1+prefixArr[r-1][c]
        return prefixArr
        