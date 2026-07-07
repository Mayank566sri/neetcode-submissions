class Solution(object):
    def isValidSudoku(self, board):

        for i in range(9):
            res = []
            ress = []
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res.append(element)
                if len(res) != len(set(res)):
                    return False

                ele = board[j][i]
                if ele != '.':
                    ress.append(ele)
                if len(ress) != len(set(ress)):
                    return False

        # Check all 3×3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                box = []
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != '.':
                            box.append(board[i][j])

                if len(box) != len(set(box)):
                    return False

        return True