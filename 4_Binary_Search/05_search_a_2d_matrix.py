class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Problem: 74. Search a 2D Matrix
        https://leetcode.com/problems/search-a-2d-matrix/

        Intuition:
        - You can treat the matrix as a long list and do binary search
        - Only need to be wary of hanlding indexes, use a helper function (first dry run with an i in the middle)
            - lets say you get i
            - row_idx should be = i//numCols
            - col_idx shoudld be = i- (row*numCols)
        
        Time:
        - O(m*n)

        Space:
        - O(1)
        """
        rows=len(matrix)
        cols=len(matrix[0])
        total=rows*cols
        st=0
        end=total-1
        while st<=end:
            idx=(end+st)//2
            r,c=self.convertIdx(idx,rows,cols)
            if matrix[r][c]>target:
                end=idx-1
            elif matrix[r][c]<target:
                st=idx+1
            else:
                return True
        return False

    def convertIdx(self,idx:int,rows:int,cols:int) -> tuple[int, int]:
        numRow=(idx)//cols
        numCols=(idx)-(numRow*cols)
        return numRow,numCols