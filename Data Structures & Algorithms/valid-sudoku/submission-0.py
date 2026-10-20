class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell != ".":
                    if cell in rows[r]:
                        return False
                    if cell in cols[c]:
                        return False
                    if cell in squares[(r // 3, c // 3)]:
                        return False
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
        return True

