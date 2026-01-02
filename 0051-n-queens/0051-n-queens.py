class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        # init a matrix with all rows and cols by zeros
        map = [["."] * n for i in range(n)]
        # init directions
        dx = [-1, -1, -1,  0,  0,  1,  1,  1]
        dy = [-1,  0,  1, -1,  1, -1,  0,  1]
        # (dx, dy) = (-1, -1)
        # check un-intersection of Queens when putting down a map
        def is_safe(row: int, col: int) -> bool:
            for i in range(8):
                r, c = row, col

                while True:
                    r += dx[i]
                    c += dy[i]

                    # check out of the map
                    if not (0 <= r < n and 0 <= c < n):
                        break
                    
                    # if checkmate with Q => fail
                    if map[r][c] == "Q":
                        return False
            return True

        def TRY(i):

            for j in range(n):

                if is_safe(i, j):
                    map[i][j] = "Q"

                    if i < n - 1:
                        TRY(i + 1)
                    else:
                        res.append(["".join(k) for k in map])
                    
                    map[i][j] = "."
        TRY(0)
        return res
