from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(10)]
        cols = [set() for _ in range(10)]
        squares = [set() for _ in range(10)]
        for row, row_vals in enumerate(board):
            for col, val in enumerate(row_vals):
                if val == ".":
                    continue
                square = int(row/3) + 3*int(col/3)
                if val in rows[row]:
                    return False
                if val in cols[col]:
                    return False
                if val in squares[square]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
                squares[square].add(val)
        return True
