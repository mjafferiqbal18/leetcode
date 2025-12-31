class NumMatrix:
    """
    Problem: 304. Range Sum Query 2D - Immutable
    https://leetcode.com/problems/range-sum-query-2d-immutable/
    
    Intuition:
        - We require O(1) time complexity, so we need to somehow use prefix sums
        - Given a (r2,c2) we need to be able ot get the sum of the complete rectangle, starting from (0,0)
        - Once we can do that, we can query other parts to get the sum bounded by (r1,c1) and (r2,c2)
        - To get the first part, we calculate the prefix sum as follows:
            - take column wise prefix sums. e.g. (2,0)= (1,0)+(0,0) and built the prefix grid
            - use these prefix grid to take row wise prefix sums: (0,2)=(0,1)+(0,0)
            - Now any (r2,c2) val in this grid is sum of rectangle bounded by (0,0) and (r,c)
        - For the second part ):
            - (i) Once we have sum[(0,0)->(r2,c2)], we subtract from it sum[(0,0)->(r1-1,c2)] (to do away with the above part)
            - (ii) Then we subtract [[(0,0)->(r2,c1-1)]-[(0,0)->(r1-1,c1-1)]] from the sum to have our final answer (to do away with left part)
                - note, we subtract [(0,0)->(r1-1,c1-1)] since it has already been counted in (i), and we do not want to double subtract it!
    
    Time Complexity:
    - O(n*n) where n is the num rows in the matrix, num rows=num cols

    Space Complexity:
    - O(n*n) where n is the num rows in the matrix, num rows=num cols
    """

    def __init__(self, matrix: List[List[int]]):
        ROWS,COLS=len(matrix),len(matrix[0])
        self.sumMat= [[0]*(COLS+1) for _ in range(ROWS+1)] #first row = all zeros, first cols is all zeros

        for r in range(ROWS):
            prefixSumRow=0
            for c in range(COLS):
                prefixSumRow+=matrix[r][c]
                above=self.sumMat[r][c+1] #get from row above
                self.sumMat[r+1][c+1]=prefixSumRow+above #r+1,c+1 cause of first row,col zeros

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: 
        #row1,col1 define topleft, row2,col2 define topright
        #add 1 offset so we can access sumMat properly
        row1+=1
        col1+=1
        row2+=1
        col2+=1

        bottomRight=self.sumMat[row2][col2]
        up=self.sumMat[row1-1][col2]
        left= self.sumMat[row2][col1-1]
        topLeft=self.sumMat[row1-1][col1-1] #since we double subtract it we need to add it back

        return bottomRight-up-left+topLeft 

        
       
       
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)