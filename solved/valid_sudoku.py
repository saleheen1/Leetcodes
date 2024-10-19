class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seenRows = set()
        seenColums = set()
        seenBoxes = set()

        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char == ".":
                    continue
                singleRow = "char "+str(char) + " at row " + str(i)
                singleColumn = "char "+ str(char) + " at column "+str(j)

                boxNumber = str(int(i)/3) + str(int(j)/3)
                # if don't have to do int(i)/3 or int(j)/3,
                # In python 3, you can import math 
                # And then do this: math.ceil(i/3) or math.ceil(j/3)
                # Which will give you integer value from decimal
                singleBox = "char "+ str(char) + " at box "+ boxNumber

                if(singleRow in seenRows or singleColumn in seenColums or singleBox in seenBoxes):
                    return False
                
                seenRows.add(singleRow)
                seenColums.add(singleColumn)
                seenBoxes.add(singleBox)

        return True





s = Solution()
board = [
 ["1","2",".",".","3",".",".",".","."],
 ["1",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
 ]

s.isValidSudoku(board=board)