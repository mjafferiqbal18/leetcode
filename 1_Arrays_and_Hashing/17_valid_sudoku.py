class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Problem: 36. Valid Sudoku
        https://leetcode.com/problems/valid-sudoku/

        Brute Force:
            Go through each row -> 9*9 -> Time: O(1) Space: 9*9 -> O(1)
            Go through each columns -> 9*9 -> Time: O(1) Space: 9*9 -> O(1)
            Go through 9 sub-blocks -> 
        
        One pass: 
            Try to visit each element (as you would for a 2d array) and perform checks 
            simultaneously for rows and columns

            The main logic here is to map co-ordinates i,j to the range 0..8, corresponding to the 9 sub-boxes
            - One can recognize that, for example, i=3 requires us to add the 3 boxes of the row above (box 0,1,2)
                - thus one aspect would be 3*(i//3)
            - lets say i=1,j=3 -> that requires us to add 1 box (column wise) since j=0,1,2 make up a box
                - another aspect would be + (j//3)
            - bringing the 2 components together, we have f(i,j)->[0..8], = 3*(i//3)+(j//3)
                - dry run on i=3,j=6: should be box=5: 3+2=5
                - similarly, i=7,j=7: should be box=8: 6+2=8

            Time: O(1)
            Space: O(1)
        """

        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        subs=[set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if (board[i][j] != "."):
                    num=int(board[i][j])
                    if (num>=1) and (num<=9): #not needed
                        if (num in rows[i]) or (num in cols[j]) or (num in subs[self.getSubBoardIdx(i,j)]):
                            return False
                        else:
                            rows[i].add(num)
                            cols[j].add(num)
                            subs[self.getSubBoardIdx(i,j)].add(num)
                    else:
                        return False 
        return True

    def getSubBoardIdx(self, i:int, j:int)->int:
        return 3*(i//3)+(j//3)
        

        